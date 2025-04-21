# -*- coding: utf-8 -*-

from .idioma import Idioma
from .pais import Pais
from .tradutor import Tradutor
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class VersaoManager(models.Manager):
    def get_by_id(self, versao_id)
    queryset = self.get_queryset()
    versao_achada = queryset.get(id=versao_id)
    return versao_achada


class Versao(models.Model):
    objects = VersaoManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    tradutor = models.ForeignKey(Tradutor, on_delete=models.DO_NOTHING, verbose_name=_('Tradutor'), db_column='tradutor_id', null=False)
    idioma = models.ForeignKey(Idioma, on_delete=models.DO_NOTHING, verbose_name=_('Idioma'), db_column='idioma_id', null=False)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, verbose_name=_('País'), db_column='pais_id', null=True)
    nome = models.CharField(max_length=128, null=False, blank=False)
    detalhes = models.TextField(verbose_name=_('Detalhes'), null=True, blank=True)
    fonte = models.CharField(max_length=2048, verbose_name=_('Fonte'), null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'versao'
        db_table_comment = 'Versões das Escrituras por idioma e tradutor'
        ordering = ['idioma__nome', 'nome']
        verbose_name = _('Versão')
        verbose_name_plural = _('Versões')
