# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class RecursoSistema:
    id = models.BigAutoField(primary_key=True, verbose_name=_('ID'), null=False)
    nome = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    detalhes = models.TextField(verbose_name=_('Detalhes'), null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'recurso_sistema'
        verbose_name = _('Recurso do Sistema')
        verbose_name_plural = _('Recursos do Sistema')
