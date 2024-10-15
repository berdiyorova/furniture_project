import modeltranslation
from django.db import models
from django.utils.translation import gettext_lazy as _

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated_at'))

    class Meta:
        abstract = True


class ContactModel(AbstractBaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(max_length=255, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'))

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


