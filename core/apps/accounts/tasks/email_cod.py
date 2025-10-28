"""
Base celery tasks
"""

import logging
from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from config.env import env


@shared_task
def EmailSendConfirm(email, code):
    try:
        message = f"""\
                Hurmatli foydalanuvchi,
                
                Sizning tasdiqlash kodingiz: {code}
                
                Ushbu kod 5 daqiqa davomida amal qiladi.
                Agar bu so‘rovni siz yubormagan bo‘lsangiz, iltimos, ushbu xabarni e’tiborsiz qoldiring.
                
                Hurmat bilan,
                Simple Travel jamoasi
                
                ---
                
                Уважаемый пользователь,
                
                Ваш код подтверждения: {code}
                
                Этот код действителен в течение 2 минут.
                Если вы не запрашивали данный код, просто проигнорируйте это сообщение.
                
                С уважением,
                Команда Simple Travel
                """
        res = send_mail(
            subject="Confirm code",
            message=message,
            from_email=env("EMAIL_HOST_USER"),
            recipient_list=[f"{email}"],
            fail_silently=False,
        )
        logging.info("Sms send: %s-%s" % (email, code))
    except Exception as e:
        logging.error(
            "Error: {email}-{code}\n\n{error}".format(email=email, code=code, error=e)
        )  # noqa
        raise Exception
