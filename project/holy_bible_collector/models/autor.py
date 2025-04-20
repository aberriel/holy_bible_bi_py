# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _


class AutorManager(models.Manager):
    pass


class Autor(models.Model):
    objects = AutorManager()

    id = models.BigAutoField(primary_key=True, verbose_name=_('ID'), null=False)
    nome = models.CharField(max_length=120, verbose_name=_('Nome'), null=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'))

    class Meta:
        db_table = 'autor'
        verbose_name = _('Autor')
        verbose_name_plural = _('Autores')
        constraints = [
            models.UniqueConstraint(fields=['nome'], name='unique_autor_nome')
        ]
