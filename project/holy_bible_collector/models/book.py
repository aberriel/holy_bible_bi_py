# -*- coding: utf-8 -*-

from .author import Author
from .bible_part import BiblePart
from .language import Language
from .version import Version
from django.db import models
from django.utils.translation import gettext as _
import uuid


class BookManager(models.Manager):
    def get_by_id(self, book_id):
        queryset = self.get_queryset()
        b = queryset.get(id=book_id)
        return b


class Livro(models.Model):
    objects = BookManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    name = models.CharField(max_length=128, verbose_name=_('Nome'), null=False)
    author = models.ForeignKey(Author, verbose_name=_('Autor'), on_delete=models.SET_NULL, db_column='author_id', null=True)
    estimated_year_written = models.CharField(max_length=9, verbose_name=_('Ano estimado da escrita'), null=True, blank=True)
    original_language = models.ForeignKey(Language, verbose_name=_('Idioma'), on_delete=models.CASCADE, db_column='language_id', null=True)
    apocryphon = models.BooleanField(verbose_name=_('É apócrifo?'), default=False, null=False)
    description = models.TextField(verbose_name=_('Descrição'), null=True)
    details = models.TextField(verbose_name=_('Detalhes'), null=True)
    bible_part = models.CharField(max_length=2, choices=BiblePart, verbose_name=_('Parte das Escrituras'), db_column='bible_part', null=False, blank=False)
    versions = models.ManyToManyField(Version, through='BookVersion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'book'
        db_table_comment = 'Livros das Escrituras'
        # uniquetogether = (('bible_part', 'name'))
        ordering = ['bible_part', 'name']
        verbose_name = _('Livro')
        verbose_name_plural = _('Livros')
        constraints = [
            models.UniqueConstraint(name='unique_part_name', fields=['bible_part', 'name'], null_distinct=True)
        ]
