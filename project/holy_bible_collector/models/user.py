# -*- coding: utf-8 -*-

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class UserManager(models.Manager):
    pass


class User(AbstractBaseUser):
    objects = UserManager()

    id = models.UUIDField('Id', primary_key=True, verbose_name=_('ID'), null=False, blank=False, default=uuid.uuid4)

    class Meta:
        db_table = 'yser'
        db_table_comment = 'Usuários do sistema'
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
