from setuptools import setup, find_packages

with open('README.md', "r") as f:
    description = f.read()

setup(
    name = 'Bigquery_Email_extractor',
    version = '0.0',
    packages = find_packages(),
    install_requires = ['google-cloud-bigquery', 'pandas'],
    entry_points = {"console_scripts" : [
        "Bigquery_Email_extractor = Bigquery_Email_extractor:bigquery_email_extractor",
    ],},
    long_description=description,
    long_description_content_type="text/markdown",
)