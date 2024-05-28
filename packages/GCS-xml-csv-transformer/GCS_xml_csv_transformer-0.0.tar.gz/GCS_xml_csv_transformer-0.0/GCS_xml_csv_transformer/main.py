import csv
import io
import xml.etree.ElementTree as ET
from google.cloud import storage


def gcs_xml_csv_transformer(BUCKET_NAME, XML_FILE_NAME, CSV_FILE_NAME):
    """
    Function to convert an XML file in a Google Cloud Storage bucket to a CSV file.

    Parameters:
    BUCKET_NAME (str): The name of the GCS bucket.
    XML_FILE_NAME (str): The name of the XML file in the GCS bucket.
    CSV_FILE_NAME (str): The name of the CSV file to be created in the GCS bucket.
    """
    
    # Initialize the GCS client
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)

    # Download the XML file from GCS
    blob = bucket.blob(XML_FILE_NAME)
    xml_data = blob.download_as_string()

    # Parse the XML data
    root = ET.fromstring(xml_data)

    # Create a buffer to hold CSV data
    with io.StringIO() as csv_buffer:
        csv_writer = csv.writer(csv_buffer)

        # Extract header from XML tags
        header = [child.tag for child in root]
        csv_writer.writerow(header)

        # Extract data from XML and write to CSV
        for child in root:
            row = [subchild.text for subchild in child]
            csv_writer.writerow(row)

        # Get CSV data as a string
        csv_data = csv_buffer.getvalue()
        print(csv_data)  # Print CSV data for debugging purposes

        # Upload the CSV data to GCS
        gcs_hook.upload(bucket_name=BUCKET_NAME, 
                        object_name=CSV_FILE_NAME,
                        data=csv_data.encode('utf-8'),
                        mime_type='text/csv')
