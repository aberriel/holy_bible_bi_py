# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _
import uuid


class Perfil(models.Model):
    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    nome = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    ativo = models.BooleanField(default=True, verbose_name=_('Está Ativo?'), null=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'perfil'
        db_table_comment = 'Perfis de usuários para a atribuição de permissões'
        ordering = ['ativo', 'nome']
        verbose_name = _('Perfil')
        verbose_name = _('Perfis')
        constraints = [
            models.UniqueConstraint(fields=['nome', 'ativo'], name='unique_perfil_ativo')
        ]
