# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _
import uuid


class AuthorManager(models.Manager):
    pass


class Author(models.Model):
    objects = Author()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    name = models.CharField(max_length=120, verbose_name=_('Nome'), null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'))

    class Meta:
        db_table = 'author'
        verbose_name = _('Autor')
        verbose_name_plural = _('Autores')
        db_table_comment = 'Autores bíblicos'
        indexes = [
            models.Index(name='index_author_name', fields=['name'])
        ]
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_author_name')
        ]
