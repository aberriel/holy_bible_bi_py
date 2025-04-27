# -*- coding: utf-8 -*-

from .country import Country
from .Language import Language
from .translator import Translator
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class VersionManager(models.Manager):
    def get_by_id(self, version_id)
    queryset = self.get_queryset()
    v = queryset.get(id=version_id)
    return v


class Version(models.Model):
    objects = VersionManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    translator = models.ForeignKey(Translator, on_delete=models.DO_NOTHING, verbose_name=_('Tradutor'), db_column='translator_id', null=False)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, verbose_name=_('Idioma'), db_column='language_id', null=False)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name=_('País'), db_column='country_id', null=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    details = models.TextField(verbose_name=_('Detalhes'), null=True, blank=True)
    source = models.CharField(max_length=2048, verbose_name=_('Fonte'), null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'version'
        db_table_comment = 'Versões das Escrituras por idioma e tradutor'
        ordering = ['language__name', 'name']
        verbose_name = _('Versão')
        verbose_name_plural = _('Versões')
