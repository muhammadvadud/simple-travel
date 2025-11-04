import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.env import env


class ConsoleEmailService:
    """Test uchun, xabarni faqat print qiladi"""

    def __init__(self) -> None:
        ...

    def send_email(self, to_email, subject, message):
        print(f"To: {to_email}\nSubject: {subject}\nMessage: {message}")


class SMTPEmailService:
    """SMTP orqali haqiqiy email yuboruvchi servis"""

    def __init__(self, host=None, port=None, username=None, password=None, use_tls=True, use_ssl=False):
        self.host = host or env("EMAIL_HOST")
        self.port = port or env.int("EMAIL_PORT")
        self.username = username or env("EMAIL_HOST_USER")
        self.password = password or env("EMAIL_HOST_PASSWORD")
        self.use_tls = env.bool("EMAIL_USE_TLS", True)
        self.use_ssl = env.bool("EMAIL_USE_SSL", False)

    def send_email(self, to_email, subject, message):
        msg = MIMEMultipart()
        msg["From"] = self.username
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))
        try:
            if self.use_ssl:
                server = smtplib.SMTP_SSL(self.host, self.port)
            else:
                server = smtplib.SMTP(self.host, self.port)
                if self.use_tls:
                    server.starttls()

            server.login(self.username, self.password)
            server.sendmail(self.username, to_email, msg.as_string())
            server.quit()
            return {"status": "success", "to": to_email}
        except Exception as e:
            return {"status": "error", "error": str(e)}
