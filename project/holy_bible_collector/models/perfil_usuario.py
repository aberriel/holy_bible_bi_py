# -*- coding: utf-8 -*-

from .perfil import Perfil
from .usuario import Usuario
from django.db import models
from django.utils.translation import gettext_laxy as _


class PerfilUsuario(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    class Meta:
        db_table = 'perfil_usuario'
        verbose_name = _('Perfil do Usuário')
        verbose_name_plural = _('Perfis dos Usuários')
