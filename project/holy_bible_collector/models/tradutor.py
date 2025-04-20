# -*- coding: utf-8 -*-

from .idioma import Idioma
from .pais import Pais
from django.db import models
from django.utils.translation import gettext_lazy as _


class TradutorManager(models.Manager):
    pass


class Tradutor(models.Model):
    objets = TradutorManager()

    id = models.BigAutoField(primary_key=True, verbose_name=_('ID'), null=False)
    idioma = models.ForeignKey(Idioma, on_delete=models.DO_NOTHING, verbose_name=_('Idioma'), null=False)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, verbose_name=_('País'), null=False)
    nome = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    class Meta:
        db_table = 'Tradutor'
        verbose_name = _('Tradutor')
        verbose_name_plural = _('Tradutores')
