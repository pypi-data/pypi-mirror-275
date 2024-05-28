from setuptools import setup, find_packages

with open('README.md', "r") as f:
    description = f.read()

setup(
    name = 'Gcs_file_dependency_monitor',
    version = '0.1',
    packages = find_packages(),
    install_requires = ['google-cloud-storage', 'datetime'],
    entry_points = {"console_scripts" : [
        "Gcs_file_dependency_monitor = Gcs_file_dependency_monitor:gcs_file_dependency_monitor",
    ],},
    long_description=description,
    long_description_content_type="text/markdown",
)