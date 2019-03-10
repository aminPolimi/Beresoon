from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=500)
    price = models.DecimalField(_('Price'), null=True)
    currency = models.CharField(_('Currency'), blank=True, null=True)
    quantity = models.FloatField(_('Quantity'), )
    unit = models.CharField(_('Unit'), max_length=100)
    part_number = models.CharField(_('Part number'), max_length=200, null=True, blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())
