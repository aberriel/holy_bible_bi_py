# -*- coding: utf-8 -*-

from .perfil import Perfil
from .usuario import Usuario
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class HistoricoPerfilUsuarioManager(models.Manager):
    pass


class HistoricoPerfilUsuario(models.Model):
    objects = HistoricoPerfilUsuarioManager()

    id = models.UUIDField(primery_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    perfil = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, db_column='perfil_id', null=True)
    nome_perfil = models.CharField(max_length=128, verbose_name=_('Nome do Perfil'), null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, db_column='usuario_id', null=True)
    nome_usuario = models.CharField(max_length=256, verbose_name=_('Nome do Usuário'), null=False, blank=False)
    data_hora_associacao = models.DateTimeField(verbose_name=_('Data e Hora da Associação'), auto_now_add=True, null=False)
    data_hora_desassociacao = models.DateTimeField(verbose_name=_('Data e Hora da Desassociação'), null=True)

    class Meta:
        db_table = 'historico_perfil_usuario'
        db_table_comment = 'Histórico de atribuições de perfis a usuários'
        ordering = ['data_hora_associacao', 'perfil__nome', 'usuario__nome']
        verbose_name = _('Registro do Histórico de Perfis do Usuário')
        verbose_name_plural = _('Histórico de Perfis do Usuário')
