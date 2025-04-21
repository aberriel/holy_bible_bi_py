# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
import uuid


class DadosBrutosManager(models.Manager):
    def get_by_id(self, dado_id):
        queryset = self.get_queryset()
        dado_original = queryset.get(id=dado_id)
        return dado_original


class DadosBrutos(models.Model):
    objects = DadosBrutosManager()

    id = models.UUIDField(primery_key=True, null=False, verbose_name=_('ID'), default=uuid.uuid4)
    fonte = models.CharField(max_length=512, null=True, verbose_name=_('Fonte'))
    idioma = models.CharField(max_length=64, null=False, blank=True, verbose_name=_('Idioma'))
    traducao = models.CharField(max_length=256, null=True, blank=True, verbose_name=_('Tradução'))
    livro = models.CharField(max_length=64, null=False, blank=False, verbose_name=_('Livro'))
    capitulo = models.IntegerField(null=False, verbose_name=_('Capítulo'))
    versiculo = models.IntegerField(null=False, verbose_name=_('Versículo'))
    texto_versiculo = models.TextField(null=False, blank=False)
    data_hora_coleta = models.DateTimeField(verbose_name=_('Data/Hora da Coleta'))

    class Meta:
        managed = True
        db_table = 'dados_brutos'
        db_table_comment = 'Dados brutos de textos bíblicos coletados de fontes externas'
        verbose_name = _('Dado Bruto')
        verbose_name_plural = _('Dados Brutos')
