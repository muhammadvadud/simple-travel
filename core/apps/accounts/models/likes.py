from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from .user import User
from core.apps.tickets.models.tickets import TicketsModel


class LikesModel(AbstractBaseModel):
    user = models.ForeignKey(User, verbose_name=_('user'), on_delete=models.CASCADE)
    ticket = models.ForeignKey(TicketsModel, verbose_name=_('ticket'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            user=User._create_fake(),
            ticket=TicketsModel._create_fake(),
        )

    class Meta:
        unique_together = ('user', 'ticket')
        db_table = "likes"
        verbose_name = _("LikesModel")
        verbose_name_plural = _("LikesModels")
