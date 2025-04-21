# -*- coding: utf-8 -*-

from .pais import Pais
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class IdiomaManager(models.Manager):
    pass


class Idioma(models.Model):
    objects = IdiomaManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    nome = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    sigla = models.CharField(max_length=10, verbose_name=_('Sigla'), null=True, blank=True)
    paises = models.ManyToManyField(Pais, through='IdiomaPais')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    def __str__(self):
        if self.sigla is not None and len(self.sigla) > 0:
            return f'{self.sigla} - {self.nome}'
        return self.nome

    class Meta:
        db_table = 'Idioma'
        db_table_comment = 'Idiomas em que as Escrituras foram escritas'
        ordering = ['nome']
        verbose_name = _('Idioma')
        verbose_name_plural = _('Idiomas')
        constraints = [
            models.UniqueConstraint(name='unique_idioma_nome_sigla', fields=['nome', 'sigla'], null_distinct=True)
        ]
