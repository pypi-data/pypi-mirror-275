import os.path
from google.cloud import storage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from datetime import datetime
import time
from email import encoders

def gcs_file_dependency_monitor(dependent_file, dependent_file_bucket,
                          number_of_tries, num_of_tries_before_warn_email, time_interval,
                          warn_email_content, warn_email_subject, email_address, error_email_content, error_email_subject,
                          SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, dependent_file_name_has_current_date = False):
    """
    Function to wait for a specific file to appear in a Google Cloud Storage bucket and send warning/error emails if it doesn't appear within a given timeframe.

    Parameters:
    dependent_file (str): The file to wait for.
    dependent_file_bucket (str): The GCS bucket containing the file.
    number_of_tries (int): The number of attempts to check for the file.
    num_of_tries_before_warn_email (int): The number of tries before sending a warning email.
    time_interval (int): The time interval (in seconds) between attempts.
    warn_email_content (str): The content of the warning email.
    warn_email_subject (str): The subject of the warning email.
    email_address (str): The recipient email address.
    error_email_content (str): The content of the error email.
    error_email_subject (str): The subject of the error email.
    SMTP_SERVER (str): The SMTP server for sending emails.
    SMTP_PORT (int): The port for the SMTP server.
    SMTP_USER (str): The SMTP server user.
    SMTP_PASSWORD (str): The SMTP server password.
    dependent_file_name_has_current_date (bool): Whether the dependent file name includes the current date.
    """
    
    wait_period = 0
    tries = 1
    tries_before_warn_email = 1
    dependency_result = False

    while tries <= int(number_of_tries):
        print("Try : ", tries)

        if dependent_file != 'None' and isinstance(dependent_file, str) and isinstance(dependent_file_bucket, str):
            # Get the directory path of the dependent file
            output_folder = os.path.dirname(dependent_file)

            # Initialize the GCS client and get the bucket
            client = storage.Client()
            bucket = client.get_bucket(dependent_file_bucket)
            print('Looking for the file, in the folder -> ', output_folder)
            output_folder = output_folder + '/'
            sources = bucket.list_blobs(prefix=output_folder, delimiter='/')

            # Extract the file name without extension
            filename_without_ext = os.path.splitext(os.path.basename(dependent_file))[0]
            
            # Get the current date
            current_dateTime = datetime.now()
            current_dateTime = current_dateTime.strftime('%Y-%m-%d')
            print('Current Datetime :', current_dateTime)
            
            if dependent_file_name_has_current_date:
                print('Expecting filename beginning from -', filename_without_ext, ',containing date ->', current_dateTime)
            else:
                print('Expecting filename beginning from -', filename_without_ext)

            # Check if the file with the expected name and current date exists in the bucket
            for blob in sources:
                if filename_without_ext in blob.name and current_dateTime in blob.name and dependent_file_name_has_current_date:
                    print(blob.name, ' has arrived')
                    dependency_result = True
                elif filename_without_ext in blob.name and dependent_file_name_has_current_date == False:
                    print(blob.name, ' has arrived')
                    dependency_result = True

        tries += 1

        if dependency_result != True:
            # Wait before sending a warning email
            if tries_before_warn_email <= int(num_of_tries_before_warn_email):
                time.sleep(int(time_interval))
                wait_period += int(time_interval)
                tries_before_warn_email += 1
                continue
            
            tries_before_warn_email = 1
            print("Wait Duration : ", wait_period, " seconds")
            
            email_content = warn_email_content + ', since ' + str(int(wait_period / 60)) + ' minutes.'
            send_email(email_address, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, warn_email_subject, email_content)
            print("Sent warning email")

            time.sleep(int(time_interval))
            wait_period += int(time_interval)
            continue
        else:
            print("Dependency has been completed.")
            tries = 1
            return True
            # break

    if tries > int(number_of_tries):
        print("Number of tries : ", tries)
        email_content = error_email_content
        send_email(email_address, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, error_email_subject, email_content)

        print('Number of tries for the dependent file has exceeded. Sent an error email.')
        return False

def send_email(RECIPIENT_EMAIL, SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SMTP_USER, SMTP_PASSWORD, EMAIL_SUBJECT, EMAIL_BODY, ATTACHMENT_FILENAME = None, csv_content = None):
    """
    Function to send an email with an optional attachment.

    Parameters:
    RECIPIENT_EMAIL (str): The recipient's email address.
    SMTP_SERVER (str): The SMTP server for sending emails.
    SMTP_PORT (int): The port for the SMTP server.
    SENDER_EMAIL (str): The sender's email address.
    SMTP_USER (str): The SMTP server user.
    SMTP_PASSWORD (str): The SMTP server password.
    EMAIL_SUBJECT (str): The subject of the email.
    EMAIL_BODY (str): The body of the email.
    ATTACHMENT_FILENAME (str, optional): The filename of the attachment. Default is None.
    csv_content (str, optional): The content of the CSV attachment. Default is None.
    """
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = EMAIL_SUBJECT
    
    # Attach the body with the msg instance
    msg.attach(MIMEText(EMAIL_BODY, 'plain'))
    
    # Create a MIMEBase instance for the attachment
    part = MIMEBase('application', 'octet-stream')
    if csv_content != None:
        part.set_payload(csv_content)
        encoders.encode_base64(part)
    if ATTACHMENT_FILENAME != None:
        part.add_header('Content-Disposition', f'attachment; filename={ATTACHMENT_FILENAME}')
        # Attach the attachment to the MIMEMultipart object
        msg.attach(part)
    
    # Send the email using the SMTP server
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
