from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from beresoon.models.users import Users


@python_2_unicode_compatible
class Setting(models.Model):
    notify_email = models.BooleanField(_('Notify email'), default=False)
    user = models.ForeignKey(Users, _("User Ber"), related_name="user_setting")#, on_delete=models.CASCADE)
    notify_app = models.BooleanField(_('Notify app'), default=True)
    notify_product_update = models.BooleanField(_('Notify product update'), default=True)
    update_date = models.DateTimeField(_('Update date'), default=datetime.now())

    class Meta:
        verbose_name = _('setting')

    def __str__(self):
        return self.user.email







