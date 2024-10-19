from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
import argilla as rg
from dotenv import load_dotenv
import os
import random
import string
import pandas as pd

from galtea.argilla_wrapper.utils import sanitize_string
from galtea.argilla_wrapper.connection.sdk_connection import SDKConnection
from .html_email_template import HTML_EMAIL_TEMPLATE

load_dotenv()

class BulkUserCreator:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_port = int(os.getenv("SMTP_PORT", default=465))
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.sender_email = os.getenv("SMTP_SENDER_EMAIL")
        self.connection = SDKConnection()

    def parse_username_from_email(self, email):
        return sanitize_string(email.split("@")[0])

    def send_mail(self, receiver, message):
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.sender_email, receiver, message)
                print(f"Email sent to {receiver}")
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
        return True

    @staticmethod
    def generate_random_string(length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_user_credentials(self, username, name, role="annotator"):
        return {
            "first_name": name.split(" ")[0],
            "last_name": name.split(" ")[1],
            "username": username,
            "password": self.generate_random_string(12),
            "role": role
        }       

    def create_argilla_user(self, user, workspace: rg.Workspace):
        return rg.User(
            username=user['username'],
            password=user['password'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            role=user['role'],
            client=self.connection._instance
        ).create().add_to_workspace(self.connection._instance.workspaces(workspace))

    def send_user_credentials_email(self, name, email, username, password):
        message = MIMEMultipart("alternative")
        message["Subject"] = "Argilla annotation tool credentials"
        message["From"] = self.sender_email
        message["To"] = email

        template = HTML_EMAIL_TEMPLATE.substitute({
            "name": name,
            "username": username,
            "password": password,
            "workspace": self.eval_workspace,
            "argilla_url": self.argilla_url
        })

        part = MIMEText(template, "html")
        message.attach(part)

        return self.send_mail(email, message.as_string())

    def create_bulk_users_from_csv(self, csv_path, workspace: rg.Workspace):
        df_users = pd.read_csv(csv_path).reset_index()  # make sure indexes pair with number of rows
        try: 
            for index, row in df_users.iterrows():
                name = row['name']
                receiver_email = row['email']
                role = row['role']
                print(f"[{index}] Sending credentials to email {receiver_email}, name {name}")

                username = self.parse_username_from_email(receiver_email)
                user = self.generate_user_credentials(username, name, role)

                argilla_user = self.create_argilla_user(user, workspace)
                
                if argilla_user.id is not None:
                    self.send_user_credentials_email(name, receiver_email, user['username'], user['password'])
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e: 
            print(f"Error: {e}")

#