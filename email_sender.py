# email_sender.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.email_config import EMAIL_CONFIG
from email_templates.email_templates import EmailTemplates

from postgre_data import dynamic_values, email_list


def send_email(to_email, subject_template, message_template, dynamic_values, sender_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject_template.format(**dynamic_values)

    # Attach the HTML message
    html_message = MIMEText(message_template, 'html')
    msg.attach(html_message)

    return msg


def send_emails(emails, dynamic_values, sender_email, smtp_server, smtp_port, sender_password):
    with smtplib.SMTP(smtp_server, smtp_port) as server:

        server.starttls()
        server.login(sender_email, sender_password)

        for i in range(len(emails)):
            subject_template = EmailTemplates.subject_template(
                dynamic_values[i]['name'])
            message_template = EmailTemplates.message_template(
                dynamic_values[i]['name'], dynamic_values[i]['employee_id'])

            msg = send_email(
                emails[i], subject_template, message_template, dynamic_values[i], sender_email)
            server.sendmail(sender_email, emails[i], msg.as_string())


# # Example usage
# dynamic_values = [{'name': 'Pavan Kumar', 'employee_id': '12345'}, {
#     'name': 'Sai Harsha', 'employee_id': '12345'}]

smtp_server = EMAIL_CONFIG['smtp_server']
smtp_port = EMAIL_CONFIG['smtp_port']
sender_email = EMAIL_CONFIG['sender_email']
sender_password = EMAIL_CONFIG['sender_password']

# Assuming you have a list of emails
# email_list = ["pavan.gattupalli@wallero.com", "sai.yada@wallero.com"]

send_emails(email_list, dynamic_values, sender_email,
            smtp_server, smtp_port, sender_password)
