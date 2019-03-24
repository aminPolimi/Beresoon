from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from beresoon.models.city import City


@python_2_unicode_compatible
class Users(User):
    photo = models.CharField(_('Photo'), null=True, blank=True, max_length=100)
    phone_number = models.CharField(null=True, max_length=20)
    selfie = models.CharField(_('Selfie'), null=True, blank=True, max_length=20)
    facebook = models.NullBooleanField(_('Facebook'), null=True)
    birth_date = models.DateField(_('Birth date'), null=True)
    passport = models.CharField(_('Passport'), null=True, blank=True, max_length=20)
    id_card = models.CharField(_('ID card'), null=True, blank=True, max_length=20)
    id_number = models.CharField(_('ID number'), null=True, blank=True, max_length=30)
    biography = models.TextField(_('Biography'), null=True, blank=True, max_length=200)

    class Meta:
        verbose_name = _('UsersBer')

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class Address(models.Model):
    city = models.ForeignKey(City, _('city'), related_name='city_address')
    street = models.CharField(_('street'), max_length=200)
    number = models.CharField(_('number'), max_length=10)
    postal_code = models.CharField(_('Postal code'), max_length=20)
    description = models.CharField(_('description'), max_length=500, null=True)
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())

    class Meta:
        verbose_name = _('address')

    def __str__(self):
        return self.city.name+' - '+self.street