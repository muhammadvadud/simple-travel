import os

PAYME_ID = os.getenv("PAYME_ID")
PAYME_KEY = os.getenv("PAYME_KEY")
PAYME_ACCOUNT_FIELD = "order_id"
PAYME_AMOUNT_FIELD = "total_price"
PAYME_ACCOUNT_MODEL = "core.apps.tickets.models.tickets.TicketorderModel"
PAYME_ONE_TIME_PAYMENT = True
