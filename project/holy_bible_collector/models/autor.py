# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _
import uuid


class AutorManager(models.Manager):
    pass


class Autor(models.Model):
    objects = AutorManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    nome = models.CharField(max_length=120, verbose_name=_('Nome'), null=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'))

    class Meta:
        db_table = 'autor'
        verbose_name = _('Autor')
        verbose_name_plural = _('Autores')
        db_table_comment = 'Autores bíblicos'
        indexes = [
            models.Index(name='index_autor_nome', fields=['nome'])
        ]
        constraints = [
            models.UniqueConstraint(fields=['nome'], name='unique_autor_nome')
        ]
