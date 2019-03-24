from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from beresoon.models.products import Products
from beresoon.models.city import City
from beresoon.models.users import Users

@python_2_unicode_compatible
class Orders(models.Model):
    product = models.ForeignKey(Products, _('product'), related_name='products_orders')#, on_delete=models.CASCADE)
    price = models.FloatField(_('Price'), null=True)
    currency = models.CharField(_('Currency'), blank=True, null=True, max_length=5)
    quantity = models.FloatField(_('Quantity'), null=True)
    unit = models.CharField(_('Unit'), max_length=100, null=True, blank=True)
    from_city = models.ForeignKey(City, _('From city'), related_name='from_orders')#, on_delete=models.PROTECT)
    to_city = models.ForeignKey(City, _('To city'), related_name='to_orders')#, on_delete=models.PROTECT)
    user = models.ForeignKey(Users, _('Requester'), related_name='user_orders')#, on_delete=models.CASCADE)
    trip_date = models.DateField(_('Trip date'), null=True)
    cancel_date = models.DateField(_('Cancel date'), null=True)
    shipment_price = models.FloatField(_('Price'))
    active = models.BooleanField(_('active'), default=True)
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())
    update_date = models.DateTimeField(_('Update date'), default=datetime.now())

    class Meta:
        verbose_name = _('orders')

    def __str__(self):
        return self.product.name


@python_2_unicode_compatible
class Offers(models.Model):
    order = models.ForeignKey(Orders, _('order'), related_name='orders_offers')#, on_delete=models.CASCADE)
    traveler = models.ForeignKey(Users, _('traveler'), related_name='traveler_offers')#, on_delete=models.CASCADE)
    price = models.FloatField(_('Price'), null=True)
    shipment_price = models.FloatField(_('Price'), null=True)
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())
    update_date = models.DateTimeField(_('Update date'), default=datetime.now())

    class Meta:
        verbose_name = _('offers')

    def __str__(self):
        return self.order.product.name




