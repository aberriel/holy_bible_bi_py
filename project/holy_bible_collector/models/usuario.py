# -*- coding: utf-8 -*-

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class UsuarioManager(models.Manager):
    pass


class Usuario(AbstractBaseUser):
    objects = UsuarioManager()

    id = models.UUIDField('Id', primary_key=True, verbose_name=_('ID'), null=False, blank=False, default=uuid.uuid4)

    class Meta:
        db_table = 'usuario'
        db_table_comment = 'Usuários do sistema'
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
