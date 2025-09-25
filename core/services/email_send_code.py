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

    def __init__(self, host=None, port=None, username=None, password=None, use_tls=True):
        self.host = host or env("EMAIL_HOST")
        self.port = port or env.int("EMAIL_PORT", 465)
        self.username = username or env("EMAIL_HOST_USER")
        self.password = password or env("EMAIL_HOST_PASSWORD")
        self.use_tls = use_tls

    def send_email(self, to_email, subject, message):
        msg = MIMEMultipart()
        msg["From"] = self.username
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))
        print("ishlayapti_Bosh")
        try:
            print("ishlayapti11")
            print(self.host, self.port)
            print("ishlayapti1112")
            server = smtplib.SMTP(self.host, self.port)
            print("ishlayapti12")
            if self.use_tls:
                print("ishlayapti34")
                server.starttls()
            print("ishlayapti")
            server.login(self.username, self.password)
            print("ishlayapt2")
            server.sendmail(self.username, to_email, msg.as_string())
            print("ishlayapt3")
            server.quit()
            print("ishlayapti4")
            return {"status": "success", "to": to_email}
        except Exception as e:
            print("ishlamayapti")

            return {"status": "error", "error": str(e)}
