# type: ignore
"""
Base celery tasks
"""

import logging
import os
from importlib import import_module

from celery import shared_task
from config.env import env
from django.utils.translation import gettext as _


@shared_task
def SendConfirm(phone, code, lang):
    """Tasdiqlash ko'dini yuborish

    Args:
        phone (str, int): telefon no'mer
        code (str, int): tasdiqlash ko'di

    Raises:
        Exception: [TODO:description]
    """

    lang = str(lang)
    OTP_MESSAGE_UZ = f"simpletravel.uz saytiga xush kelibsiz! Sizning tasdiqlash kodingiz - {code} "
    OTP_MESSAGE_RU = f"Dobro pojalovat na sayt simpletravel.uz! Vash kod podtverjdeniya - {code}"
    try:
        service = getattr(
            import_module(os.getenv("OTP_MODULE")), os.getenv("OTP_SERVICE")
        )()
        if lang.lower() == "ru":
            message = OTP_MESSAGE_RU
        else:
            message = OTP_MESSAGE_UZ
        service.send_sms(phone, message)
        logging.info("Sms send: %s-%s" % (phone, code))
    except Exception as e:
        logging.error(
            "Error: {phone}-{code}\n\n{error}".format(phone=phone, code=code, error=e)
        )  # noqa
        raise Exception
