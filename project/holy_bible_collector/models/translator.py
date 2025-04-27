# -*- coding: utf-8 -*-

from .country import Country
from .language import Language
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class TranslatorManager(models.Manager):
    pass


class Translator(models.Model):
    objets = TradutorManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, verbose_name=_('Idioma'), db_column='language_id', null=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name=_('País'), db_column='country_id', null=False)
    name = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    class Meta:
        db_table = 'translator'
        db_table_comment = 'Tradutores das Escrituras'
        ordering = ['language__name', 'country__name', 'name']
        verbose_name = _('Tradutor')
        verbose_name_plural = _('Tradutores')
