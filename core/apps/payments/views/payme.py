from payme.views import PaymeWebHookAPIView
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from payme.models import PaymeTransactions
from core.apps.tickets.models.tickets import TicketorderModel
from core.apps.tickets.choices.order import OrderStatusChoices


@extend_schema(tags=["payments"])
class PaymeCallBackAPIView(PaymeWebHookAPIView):
    permission_classes = [AllowAny]

    def handle_created_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction created for this params: {params} and cr_result: {result}")

    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        try:
            transaction_id = params.get("id")
            transaction = PaymeTransactions.objects.filter(transaction_id=transaction_id).first()
            order = TicketorderModel.objects.get(id=transaction.account_id)
            order.order_status = OrderStatusChoices.PENDING_CONFIRMATION
            order.save()
        except TicketorderModel.DoesNotExist:
            print(f"Order with ID not found.")
        except Exception as e:
            print(f"===========\n\n{e}\n\n========================")

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        try:
            transaction_id = params.get("id")
            transaction = PaymeTransactions.objects.filter(transaction_id=transaction_id).first()
            order = TicketorderModel.objects.get(id=transaction.account_id)
            order.order_status = OrderStatusChoices.CANCELLED
            order.save()
        except TicketorderModel.DoesNotExist:
            print(f"Order with ID not found.")
        except Exception as e:
            print(f"===========\n\n{e}\n\n========================")
