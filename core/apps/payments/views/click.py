from click_up.views import ClickWebhook
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny


@extend_schema(tags=["payments"])
class ClickWebhookAPIView(ClickWebhook):
    permission_classes = [AllowAny]

    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """
        print(f"payment successful params: {params}")

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        print(f"payment cancelled params: {params}")
