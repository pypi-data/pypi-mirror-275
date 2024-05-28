from google.cloud import bigquery
import pandas as pd
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def bigquery_email_extractor(BQ_PROJECT_ID, BQ_DATASET_ID, BQ_TABLE_ID, RECIPIENT_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, EMAIL_SUBJECT, EMAIL_BODY, ATTACHMENT_FILENAME):
    """
    Function to extract data from BigQuery and send it as a CSV attachment via email.

    Parameters:
    BQ_PROJECT_ID (str): The BigQuery project ID.
    BQ_DATASET_ID (str): The BigQuery dataset ID.
    BQ_TABLE_ID (str): The BigQuery table ID.
    RECIPIENT_EMAIL (str): The recipient email address.
    SMTP_SERVER (str): The SMTP server for sending emails.
    SMTP_PORT (int): The port for the SMTP server.
    SMTP_USER (str): The SMTP server user.
    SMTP_PASSWORD (str): The SMTP server password.
    EMAIL_SUBJECT (str): The subject of the email.
    EMAIL_BODY (str): The body of the email.
    ATTACHMENT_FILENAME (str): The filename for the CSV attachment.
    """
    
    # Initialize BigQuery client
    bigquery_client = bigquery.Client(project=BQ_PROJECT_ID)
    table_ref = bigquery_client.dataset(BQ_DATASET_ID).table(BQ_TABLE_ID)
    table = bigquery_client.get_table(table_ref)

    # Extract data into a pandas DataFrame (requires pandas library)
    df = bigquery_client.list_rows(table).to_dataframe()

    # Convert DataFrame to CSV string
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_string = csv_buffer.getvalue()
    csv_content = csv_string.encode('utf-8')

    # Send the extracted data via email
    send_email(csv_content, RECIPIENT_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, EMAIL_SUBJECT, EMAIL_BODY, ATTACHMENT_FILENAME)


def send_email(csv_content, RECIPIENT_EMAIL, SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SMTP_USER, SMTP_PASSWORD, EMAIL_SUBJECT, EMAIL_BODY, ATTACHMENT_FILENAME = None):
    """
    Function to send an email with an optional attachment.

    Parameters:
    csv_content (bytes): The CSV content to be attached.
    RECIPIENT_EMAIL (str): The recipient's email address.
    SMTP_SERVER (str): The SMTP server for sending emails.
    SMTP_PORT (int): The port for the SMTP server.
    SENDER_EMAIL (str): The sender's email address.
    SMTP_USER (str): The SMTP server user.
    SMTP_PASSWORD (str): The SMTP server password.
    EMAIL_SUBJECT (str): The subject of the email.
    EMAIL_BODY (str): The body of the email.
    ATTACHMENT_FILENAME (str, optional): The filename of the attachment. Default is None.
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
    if csv_content is not None:
        part.set_payload(csv_content)
        encoders.encode_base64(part)
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
