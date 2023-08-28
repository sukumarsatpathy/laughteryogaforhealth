from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    fullName = models.CharField(_('Full Name'), max_length=500, null=True)
    email = models.EmailField(_('Email'), max_length=500, null=True)
    message = models.TextField(_('Message'), null=True)
    submitted_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created Date')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
        db_table = 'contact_list'

    def __str__(self):
        return self.fullName


class Invite(models.Model):
    fullName = models.CharField(_('Full Name'), max_length=500, null=True)
    email = models.EmailField(_('Email'), max_length=500, null=True)
    contact = models.CharField(_('Contact'), max_length=20, null=True)
    country = models.CharField(_('Country'), max_length=100, null=True)
    message = models.TextField(_('Message'), null=True)
    submitted_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created Date')

    class Meta:
        verbose_name = 'Invite'
        verbose_name_plural = 'Invite'
        db_table = 'invite_list'

    def __str__(self):
        return self.fullName


class Newsletter(models.Model):
    email = models.EmailField(_('Email'), max_length=500)
    status = models.BooleanField(_('Status'), default=True)
    submitted_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created Date')

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'
        db_table = 'newsletter_list'

    def __str__(self):
        return self.email