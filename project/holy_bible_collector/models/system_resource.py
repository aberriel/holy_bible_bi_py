# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class RecursoSistema:
    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    name = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    details = models.TextField(verbose_name=_('Detalhes'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'system_resource'
        ordering = ['name']
        verbose_name = _('Recurso do Sistema')
        verbose_name_plural = _('Recursos do Sistema')
