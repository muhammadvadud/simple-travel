from django.db.models.signals import post_save
from django.dispatch import receiver
from click_up.models import ClickTransaction


@receiver(post_save, sender=ClickTransaction)
def handle_click_transaction(sender, instance, created, **kwargs):
    """
    Click to'lov holati o'zgarganda signal ishlaydi
    """
    if instance.state == ClickTransaction.SUCCESSFULLY:
        print("✅ Click to'lovi muvaffaqiyatli yakunlandi:", instance.transaction_id)

    elif instance.state == ClickTransaction.CANCELLED:
        print("❌ Click to'lovi bekor qilindi:", instance.transaction_id)
