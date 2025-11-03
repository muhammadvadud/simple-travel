from django.db.models.signals import post_save
from django.dispatch import receiver
from payme.models import PaymeTransactions
from core.apps.dashboard.models import AgencyReport
from core.apps.accounts.models import TravelAgency
from core.apps.tickets.models import TicketorderModel
from core.apps.dashboard.choices.agency_report import AgencyReportPaymentChoices


@receiver(post_save, sender=PaymeTransactions)
def handle_payme_transaction(sender, instance, created, **kwargs):
    """
    Payme to'lov holati o'zgarganda signal ishlaydi
    """
    try:
        order = TicketorderModel.objects.get(id=instance.account_id)
        agency = order.ticket.travel_agency

    except TicketorderModel.DoesNotExist:
        print(f"⚠️ Order topilmadi: {instance.account_id}")
        return
    except TravelAgency.DoesNotExist:
        print(f"⚠️ TravelAgency topilmadi: {instance.account_id}")
        return

    if instance.state == PaymeTransactions.SUCCESSFULLY:
        print("✅ Payme to'lovi muvaffaqiyatli yakunlandi:", instance.transaction_id)
        real_amount = int(instance.amount) // 100
        AgencyReport.create_report(
            agency=agency,
            total_income=real_amount,
            order=order,
            payment_method=AgencyReportPaymentChoices.PAYME
        )

    elif instance.state in [PaymeTransactions.CANCELED, PaymeTransactions.CANCELED_DURING_INIT]:
        print("❌ Payme to'lovi bekor qilindi:", instance.transaction_id)

        AgencyReport.delete_report(order)
