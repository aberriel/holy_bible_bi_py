# -*- coding: utf-8 -*-

from .book import Book
from .version import Version
from django.db import models
from django.utils.translation import gettext as _
import uuid


class BookVersionManager(models.Manager):
    pass


class LivroVersao(models.Model):
    objects = BookVersionManager()

    id = models.UUIDField('Id', primary_key=True, verbose_name=_('ID'), null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('Livro'), db_column='book_id', null=False)
    version = models.ForeignKey(Version, on_delete=models.CASCADE, verbose_name=_('Versão'), db_column='version_id', null=False)
    source = models.CharField(max_length=2048, verbose_name=_('Fonte'), null=True, blank=True)
    version_name = models.CharField(max_length=512, verbose_name=_('Nome do Livro na Versão'), null=True, blank=True)
    details = models.TextField(verbose_name=_('Detalhes'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'book_version'
        db_table_comment = 'Relaciona os livros das Escrituras com as versões nas quais estão disponíveis'
        ordering = ['book__name', 'version__name', 'version_name']
        verbose_name = _('Versão do Livro')
        verbose_name_plural = _('Versões dos Livros')
