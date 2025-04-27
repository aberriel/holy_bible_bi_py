# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _
import uuid


class ProfileManager(models.Manager):
    pass


class Profile(models.Model):
    objects = ProfileManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    name = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    active = models.BooleanField(default=True, verbose_name=_('Está Ativo?'), null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'profile'
        db_table_comment = 'Perfis de usuários para a atribuição de permissões'
        ordering = ['active', 'name']
        verbose_name = _('Perfil')
        verbose_name = _('Perfis')
        constraints = [
            models.UniqueConstraint(fields=['name', 'active'], name='unique_profile_active')
        ]
