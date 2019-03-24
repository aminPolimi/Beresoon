from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


@python_2_unicode_compatible
class Products(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    code = models.CharField(_('Code'), max_length=50, null=True, blank=True)
    price = models.FloatField(_('Price'), null=True)
    currency = models.CharField(_('Currency'), blank=True, null=True, max_length=5)
    quantity = models.FloatField(_('Quantity'), null=True)
    unit = models.CharField(_('Unit'), max_length=100, null=True, blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())
    update_date = models.DateTimeField(_('Update date'), default=datetime.now())
    url = models.CharField(_('Name'), max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = _('products')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Photos(models.Model):
    location = models.CharField(_('Name'), max_length=10)
    product = models.ForeignKey(Products, _('product'), related_name='products_photos')

    class Meta:
        verbose_name = _('photos')

    def __str__(self):
        return self.location
