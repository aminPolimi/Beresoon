from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_mysql.models import EnumField
from datetime import datetime
from beresoon.models.orders import Offers
from beresoon.models.users import Address

@python_2_unicode_compatible
class Purchase(models.Model):
    offer = models.ForeignKey(Offers, _('offer'), related_name='offers_purchase')#, on_delete=models.PROTECT)
    submit_date = models.DateTimeField(_('Submit date'), default=datetime.now())
    deliver_date = models.DateTimeField(_('Deliver date'))
    deliver_address = models.ForeignKey(Address, _('address'), related_name='address_purchase', null=True)#
                                        # , on_delete=models.PROTECT)
    active = models.BooleanField(_('active'), default=True)
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())
    update_date = models.DateTimeField(_('Update date'), default=datetime.now())

    class Meta:
        verbose_name = _('orders')

    def __str__(self):
        return self.product.name


@python_2_unicode_compatible
class CancelPurchase(models.Model):
    purchase = models.ForeignKey(Purchase, _('purchase'), related_name='purchase_cancel', on_delete=models.SET_NULL)
    requester_date = models.DateTimeField(_('Requester date'), null=True)
    traveler_date = models.DateTimeField(_('Traveler date'), null=True)
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())
    active = models.NullBooleanField(_('active'), null=True)

    class Meta:
        verbose_name = _('Cancel purchase')

    def __str__(self):
        return self.order.product.name


@python_2_unicode_compatible
class Rate(models.Model):
    purchase = models.ForeignKey(Purchase, _('purchase'), related_name='purchase_rate', on_delete=models.SET_NULL)
    comment = models.TextField(_('comment'))
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())
    value = EnumField(choices=[(1, _(1)), (2, _(2)), (3, _(3)), (4, _(4)), (5, _(5))],
                      verbose_name=_("Type accuracy"), null=True)
    user_type = EnumField(choices=[('requester', _('requester')), ('traveler', _('traveler'))],
                      verbose_name=_("Type accuracy"), null=True)

    class Meta:
        verbose_name = _('rate')

    def __str__(self):
        return self.comment

