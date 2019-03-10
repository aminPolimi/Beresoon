from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, AbstractUser

@python_2_unicode_compatible
class Users(User):
    biography = models.TextField(_('Biography'), null=True, blank=True)

    class Meta:
        verbose_name = _('users')

    def __str__(self):
        return self.username
