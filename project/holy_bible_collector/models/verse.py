# -*- coding: utf-8 -*-

from .book_version import BookVersion
from .chapter import Chapter
from .language import Language
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class VerseManager(models.Manager):
    pass


class Verse(models.Model):
    objects = VersiculoManager()

    id = models.UUIDField(primery_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('Capítulo'), db_column='chapter_id', null=False)
    book_version = models.ForeignKey(BookVersion, on_delete=models.CASCADE, verbose_name=_('Livro/Versão'), db_column='book_version_id', null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name=_('Idioma'), db_column='language_id', null=False)
    content = models.TextField(verbose_name=_('Texto do Versículo'), null=False, blank=False)
    source = models.CharField(max_length=2048, verbose_name=_('Fonte'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'))

    class Meta:
        db_table = 'verse'
        db_table_comment = 'Os versos das Escrituras'
        ordering = ['language__name', 'book_version__book__bible_part', 'book_version__book__name', 'chapter__number']
        verbose_name = _('Versículo')
        verbose_name_plural = _('Versículos')
