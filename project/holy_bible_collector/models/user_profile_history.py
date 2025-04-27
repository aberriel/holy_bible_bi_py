# -*- coding: utf-8 -*-

from .profile import Profile
from .user import User
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class UserProfileHistoryManager(models.Manager):
    pass


class UserProfileHistory(models.Model):
    objects = UserProfileHistoryManager()

    id = models.UUIDField(primery_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, db_column='profile_id', null=True)
    profile_name = models.CharField(max_length=128, verbose_name=_('Nome do Perfil'), null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id', null=True)
    user_name = models.CharField(max_length=256, verbose_name=_('Nome do Usuário'), null=False, blank=False)
    associated_at = models.DateTimeField(verbose_name=_('Data e Hora da Associação'), auto_now_add=True, null=False)
    disassociated_at = models.DateTimeField(verbose_name=_('Data e Hora da Desassociação'), null=True)

    class Meta:
        db_table = 'user_profile_history'
        db_table_comment = 'Histórico de atribuições de perfis a usuários'
        ordering = ['associated_at', 'profile__name', 'user__name']
        verbose_name = _('Registro do Histórico de Perfis do Usuário')
        verbose_name_plural = _('Histórico de Perfis do Usuário')
