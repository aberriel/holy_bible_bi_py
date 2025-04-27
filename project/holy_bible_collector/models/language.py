# -*- coding: utf-8 -*-

from .country import Country
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class LanguageManager(models.Manager):
    pass


class Language(models.Model):
    objects = LanguageManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    name = models.CharField(max_length=128, verbose_name=_('Nome'), null=False, blank=False)
    abbreviation = models.CharField(max_length=10, verbose_name=_('Sigla'), null=True, blank=True)
    countries = models.ManyToManyField(Country, through='IdiomaPais')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    def __str__(self):
        if self.abbreviation is not None and len(self.abbreviation) > 0:
            return f'{self.abbreviation} - {self.name}'
        return self.name

    class Meta:
        db_table = 'language'
        db_table_comment = 'Idiomas em que as Escrituras foram escritas'
        ordering = ['name']
        verbose_name = _('Idioma')
        verbose_name_plural = _('Idiomas')
        constraints = [
            models.UniqueConstraint(name='unique_language_name_abbreviation', fields=['name', 'abbreviation'], null_distinct=True)
        ]
