from setuptools import setup, find_packages

with open('README.md', "r") as f:
    description = f.read()

setup(
    name = 'GCS_xml_csv_transformer',
    version = '0.0',
    packages = find_packages(),
    install_requires = ['google-cloud-storage'],
    entry_points = {"console_scripts" : [
        "GCS_xml_csv_transformer = GCS_xml_csv_transformer:gcs_xml_csv_transformer",
    ],},
    long_description=description,
    long_description_content_type="text/markdown",
)