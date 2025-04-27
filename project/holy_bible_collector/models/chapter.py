# -*- coding: utf-8 -*-

from .book import Book
from django.db import models
from django.utils.translation import gettext as _
import uuid


class ChapterManager(models.Manager):
    def get_by_id(self, chapter_id):
        queryset = self.get_queryset()
        c = queryset.get(id=chapter_id)
        return c


class Chapter(models.Model):
    objects = ChapterManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    book = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name=_('Livro'), db_column='book_id', null=False, blank=False)
    number = models.IntegerField(verbose_name=_('Número'), null=False)
    apocryphon = models.BooleanField(verbose_name=_('É apócrifo?'), null=False, default=False)
    details = models.TextField(verbose_name=_('Detalhes'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    class Meta:
        db_table = 'chapter'
        db_table_comment = 'Capítulos dos livros das Escrituras'
        ordering = ['book__bible_part', 'book__name', 'number']
        verbose_name = _('Capítulo')
        verbose_name_plural = _('Capítulos')
