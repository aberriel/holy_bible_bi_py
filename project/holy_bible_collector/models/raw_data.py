# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
import uuid


class RawDataManager(models.Manager):
    def get_by_id(self, data_id):
        queryset = self.get_queryset()
        original_data = queryset.get(id=data_id)
        return original_data


class DadosBrutos(models.Model):
    objects = DadosBrutosManager()

    id = models.UUIDField(primery_key=True, null=False, verbose_name=_('ID'), default=uuid.uuid4)
    source = models.CharField(max_length=512, null=True, verbose_name=_('Fonte'))
    language = models.CharField(max_length=64, null=False, blank=True, verbose_name=_('Idioma'))
    translation = models.CharField(max_length=256, null=True, blank=True, verbose_name=_('Tradução'))
    book = models.CharField(max_length=64, null=False, blank=False, verbose_name=_('Livro'))
    chapter = models.IntegerField(null=False, verbose_name=_('Capítulo'))
    verse = models.IntegerField(null=False, verbose_name=_('Versículo'))
    verse_content = models.TextField(null=False, blank=False)
    collected_at = models.DateTimeField(verbose_name=_('Data/Hora da Coleta'))

    class Meta:
        managed = True
        db_table = 'raw_data'
        db_table_comment = 'Dados brutos de textos bíblicos coletados de fontes externas'
        verbose_name = _('Dado Bruto')
        verbose_name_plural = _('Dados Brutos')
