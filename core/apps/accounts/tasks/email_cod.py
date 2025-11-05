"""
Base celery tasks
"""

import logging
from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from config.env import env
from datetime import datetime


@shared_task
def EmailSendConfirm(email, code):
    try:
        message = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8" />
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f5f5f7;
                    margin: 0;
                    padding: 0;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: auto;
                    background-color: #ffffff;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background-color: #0d6efd;
                    padding: 20px;
                    text-align: center;
                    color: #ffffff;
                }}
                .header img {{
                    width: 120px;
                    margin-bottom: 10px;
                }}
                .content {{
                    padding: 25px;
                    color: #333;
                    font-size: 15px;
                    line-height: 1.6;
                }}
                .code-box {{
                    background-color: #f0f4ff;
                    border: 1px solid #0d6efd;
                    padding: 15px;
                    font-size: 20px;
                    text-align: center;
                    font-weight: bold;
                    letter-spacing: 2px;
                    border-radius: 8px;
                    color: #0d6efd;
                    margin: 20px 0;
                }}
                .footer {{
                    font-size: 13px;
                    text-align: center;
                    color: #888;
                    padding: 20px;
                }}
                .divider {{
                    border-top: 1px solid #ddd;
                    margin: 25px 0;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <img src="https://simpletravel.uz/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FLogoWhite.98021d99.png&w=128&q=75" alt="Simple Travel Logo" />
                    <h2>Simple Travel</h2>
                </div>
                <div class="content">
                    <p>Hurmatli foydalanuvchi,</p>
                    <p>Sizning tasdiqlash kodingiz:</p>
                    <div class="code-box">{code}</div>
                    <p>Ushbu kod <strong>2 daqiqa</strong> davomida amal qiladi.<br>
                    Agar bu so‘rovni siz yubormagan bo‘lsangiz, iltimos, ushbu xabarni e’tiborsiz qoldiring.</p>

                    <p>Hurmat bilan,<br><strong>Simple Travel jamoasi</strong></p>

                    <div class="divider"></div>

                    <p><strong>Уважаемый пользователь,</strong></p>
                    <p>Ваш код подтверждения:</p>
                    <div class="code-box">{code}</div>
                    <p>Этот код действителен в течение <strong>2 минут</strong>.<br>
                    Если вы не запрашивали данный код, просто проигнорируйте это сообщение.</p>

                    <p>С уважением,<br><strong>Команда Simple Travel</strong></p>
                </div>

                <div class="footer">
                    © {datetime.now().year} Simple Travel. Barcha huquqlar himoyalangan.<br>
                    Bu avtomatik xabar. Iltimos, javob yozmang.
                </div>
            </div>
        </body>
        </html>
        """

        # res = send_mail(
        #     subject="Confirm code",
        #     message=message,
        #     from_email=env("EMAIL_HOST_USER"),
        #     recipient_list=[f"{email}"],
        #     fail_silently=False,
        # )
        from_name = "Simple Travel"
        from_email = f"{from_name} <{env('EMAIL_HOST_USER')}>"

        email_message = EmailMessage(
            subject="Simple Travel — Tasdiqlash kodi",
            body=message,
            from_email=from_email,
            to=[email],
        )
        email_message.content_subtype = "html"
        email_message.send()
        logging.info("Email  send: %s-%s" % (email, code))
    except Exception as e:
        logging.error(
            "Error: {email}-{code}\n\n{error}".format(email=email, code=code, error=e)
        )  # noqa
        raise Exception
