from click_up.views import ClickWebhook
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from click_up.models import ClickTransaction
from core.apps.tickets.models.tickets import TicketorderModel
from core.apps.tickets.choices.order import OrderStatusChoices
from core.apps.dashboard.models import AgencyReport


@extend_schema(tags=["payments"])
class ClickWebhookAPIView(ClickWebhook):
    permission_classes = [AllowAny]

    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """
        try:
            transaction_id = params.click_trans_id
            transaction = ClickTransaction.objects.filter(transaction_id=transaction_id).first()
            order = TicketorderModel.objects.get(id=transaction.account_id)
            order.order_status = OrderStatusChoices.PENDING_CONFIRMATION
            order.save()
        except TicketorderModel.DoesNotExist:
            print(f"Order with ID not found.")
        except Exception as e:
            print(f"===========\n\n{e}\n\n========================")

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        try:
            transaction_id = params.click_trans_id
            print("❌ Click to'lovi bekor qilindi:", transaction_id)
            transaction = ClickTransaction.objects.filter(transaction_id=transaction_id).first()
            order = TicketorderModel.objects.get(id=transaction.account_id)
            AgencyReport.delete_report(order)
            order.order_status = OrderStatusChoices.CANCELLED
            order.save()
        except TicketorderModel.DoesNotExist:
            print(f"Order with ID not found.")
        except Exception as e:
            print(f"===========\n\n{e}\n\n========================")
