from django.db.models.signals import post_save
from django.dispatch import receiver
from click_up.models import ClickTransaction
from core.apps.tickets.models import TicketorderModel
from core.apps.accounts.models import TravelAgency
from core.apps.dashboard.choices import AgencyReportPaymentChoices
from core.apps.dashboard.models import AgencyReport


@receiver(post_save, sender=ClickTransaction)
def handle_click_transaction(sender, instance, created, **kwargs):
    """
    Click_up to'lov holati o'zgarganda signal ishlaydi
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

    if instance.state == ClickTransaction.SUCCESSFULLY:
        print("✅ Click_up to'lovi muvaffaqiyatli yakunlandi:", instance.transaction_id)

        AgencyReport.create_report(
            agency=agency,
            total_income=int(instance.amount),
            order=order,
            payment_method=AgencyReportPaymentChoices.CLICK,
        )

