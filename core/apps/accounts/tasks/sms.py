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
def SendConfirm(phone, code, lang, type):
    """
    Tasdiqlash ko'dini yuborish
    type: "register" yoki "reset_password"
    lang: "uz" yoki "ru"
    """

    lang = str(lang).lower()
    type = str(type).lower()

    MESSAGES = {
        "register": {
            "uz": f"simpletravel.uz saytiga xush kelibsiz! Sizning tasdiqlash kodingiz - {code}",
            "ru": f"Dobro pojalovat na sayt simpletravel.uz! Vash kod podtverjdeniya - {code}",
        },
        "reset_password": {
            "uz": f"simpletravel.uz saytida parolni tiklash kodi: {code}",
            "ru": f"Kod vosstanovleniya parolya na sayte simpletravel.uz: {code}",
        },
    }

    try:
        service = getattr(
            import_module(os.getenv("OTP_MODULE")),
            os.getenv("OTP_SERVICE")
        )()

        message = MESSAGES.get(type, MESSAGES["register"]).get(lang, MESSAGES["register"]["uz"])

        service.send_sms(phone, message)
        logging.info("Sms send: %s-%s" % (phone, code))

    except Exception as e:
        logging.error(f"Error: {phone}-{code}\n\n{e}")
        raise Exception
