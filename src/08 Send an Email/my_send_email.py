#dont want to provide my info and also never worked with
#smtp, so just find the solution on the internet

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(recipient_email, subject, message_body):
    # SMTP server settings (replace with your own server and credentials)
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Sender's email address
    sender_email = 'your_email@example.com'

    # Create a MIMEText object for the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS for security
        server.login(smtp_username, smtp_password)  # Login to the server

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the SMTP server connection
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


# Example usage:
if __name__ == "__main__":
    recipient_email = 'recipient@example.com'
    subject = 'Hello, World!'
    message_body = 'This is a test email from Python.'

    send_email(recipient_email, subject, message_body)
