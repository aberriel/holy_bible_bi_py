# -*- coding: utf-8 -*-

from .idioma import Idioma
from .pais import Pais
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class TradutorManager(models.Manager):
    pass


class Tradutor(models.Model):
    objets = TradutorManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, verbose_name=_('Idioma'), db_column='idioma_id', null=False)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, verbose_name=_('País'), db_column='pais_id', null=False)
    nome = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    class Meta:
        db_table = 'Tradutor'
        db_table_comment = 'Tradutores das Escrituras'
        ordering = ['idioma__nome', 'pais__nome', 'nome']
        verbose_name = _('Tradutor')
        verbose_name_plural = _('Tradutores')
