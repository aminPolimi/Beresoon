from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    code = models.CharField(_('Code'), max_length=4)
    phone_code = models.CharField(_('Phone code'), max_length=4)

    class Meta:
        verbose_name = _('country')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    code = models.CharField(_('Code'), max_length=5)
    phone_code = models.CharField(_('Phone code'), max_length=5)
    country = models.ForeignKey(Country, _('country'), related_name='city_country')#, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('city')

    def __str__(self):
        return self.name