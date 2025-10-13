import os

CLICK_SERVICE_ID = os.getenv("CLICK_SERVICE_ID")
CLICK_MERCHANT_ID = os.getenv("CLICK_MERCHANT_ID")
CLICK_SECRET_KEY = os.getenv("CLICK_SECRET_KEY")
CLICK_ACCOUNT_MODEL = "core.apps.tickets.models.tickets.TicketorderModel"
CLICK_AMOUNT_FIELD = "total_price"

CLICK_COMMISSION_PERCENT = "(optional int field) your companies comission percent if applicable"
CLICK_DISABLE_ADMIN = False
