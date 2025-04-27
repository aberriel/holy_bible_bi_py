# -*- coding: utf-8 -*-

from .perfil import Perfil
from .usuario import Usuario
from django.db import models
from django.utils.translation import gettext_laxy as _


class UserProfile(models.Model):
    profile = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='profile_id', null=False, blank=False)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='user_id', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    class Meta:
        db_table = 'user_profile'
        db_table_comment = 'Tabela associativa entre perfis e usuários'
        verbose_name = _('Perfil do Usuário')
        verbose_name_plural = _('Perfis dos Usuários')
