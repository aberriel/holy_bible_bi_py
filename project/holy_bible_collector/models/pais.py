# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class PaisManager(models.Manager):
    pass


class Pais(models.Model):
    objects = PaisManager()

    id = models.BigAutoField(primery_key=True, verbose_name=_('ID'), null=False)
    nome = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    sigla = models.CharField(max_length=5, verbose_name=_('Sigla'), null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'pais'
        verbose_name = _('País')
        verbose_name_plural = _('Países')
