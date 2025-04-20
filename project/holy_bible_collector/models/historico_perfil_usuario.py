# -*- coding: utf-8 -*-

from .perfil import Perfil
from .usuario import Usuario
from django.db import models
from django.utils.translation import gettext_lazy as _


class HistoricoPerfilUsuarioManager(models.Manager):
    pass


class HistoricoPerfilUsuario(models.Model):
    objects = HistoricoPerfilUsuarioManager()

    id = models.BigAutoField(primery_key=True, verbose_name=_('ID'), null=False)
    perfil = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
    nome_perfil = models.CharField(max_length=128, verbose_name=_('Nome do Perfil'), null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    nome_usuario = models.CharField(max_length=256, verbose_name=_('Nome do Usuário'), null=False, blank=False)
    data_hora_associacao = models.DateTimeField(verbose_name=_('Data e Hora da Associação'), auto_now_add=True, null=False)
    data_hora_desassociacao = models.DateTimeField(verbose_name=_('Data e Hora da Desassociação'), null=True)

    class Meta:
        db_table = 'historico_perfil_usuario'
