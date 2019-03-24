from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from beresoon.models.city import City


@python_2_unicode_compatible
class Travels(models.Model):
    from_city = models.ForeignKey(City, _('From city'), related_name='from_orders')#, on_delete=models.PROTECT)
    to_city = models.ForeignKey(City, _('To city'), related_name='to_orders')#, on_delete=models.PROTECT)
    from_date = models.DateField(_('From date'), null=True)
    to_date = models.DateField(_('To date'))
    register_date = models.DateTimeField(_('Register date'), default=datetime.now())
    notify = models.BooleanField(_('Notify'), default=True)

    class Meta:
        verbose_name = _('travels')

    def __str__(self):
        return self.from_city.name+' - '+self.to_city.name
