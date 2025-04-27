# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class CountryManager(models.Manager):
    pass


class Country(models.Model):
    objects = CountryManager()

    id = models.UUIDField(primery_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    name = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    abbreviation = models.CharField(max_length=5, verbose_name=_('Sigla'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'country'
        db_table_comment = 'Relação de países para os quais as Escrituras foram traduzidas'
        ordering = ['name']
        verbose_name = _('País')
        verbose_name_plural = _('Países')
