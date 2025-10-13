from payme import Payme
from click_up import ClickUp
import os


def get_payme_url(order_id, amount, return_url):
    payme_id = os.getenv('PAYME_ID')
    payme = Payme(payme_id=payme_id)
    pay_link = payme.initializer.generate_pay_link(id=order_id, amount=amount, return_url=return_url)
    return pay_link


def get_click_url(order_id, amount, return_url):
    click_service_id = os.getenv("CLICK_SERVICE_ID")
    click_merchant_id = os.getenv("CLICK_MERCHANT_ID")

    click_up = ClickUp(
        service_id=click_service_id,
        merchant_id=click_merchant_id
    )
    paylink = click_up.initializer.generate_pay_link(
        id=order_id,
        amount=amount,
        return_url=return_url
    )
    return paylink
