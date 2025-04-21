# -*- coding: utf-8 -*-

from .livro import Livro
from django.db import models
from django.utils.translation import gettext as _
import uuid


class CapituloManager(models.Manager):
	def get_by_id(self, capitulo_id):
		queryset = self.get_queryset()
		capitulo = queryset.get(id=capitulo_id)
		return capitulo


class Capitulo(models.Model):
	id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name=_('Livro'), db_column='livro_id', null=False, blank=False)
	numero = models.IntegerField(verbose_name=_('Número'), null=False)
	apocrifo = models.BooleanField(verbose_name=_('É apócrifo?'), null=False, default=False)
	detalhes = models.TextField(verbose_name=_('Detalhes'), null=True, blank=True)
	criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

	class Meta:
		db_table = 'capitulo'
		db_table_comment = 'Capítulos dos livros das Escrituras'
		ordering = ['livro__parte_biblia', 'livro__nome', 'numero']
		verbose_name = _('Capítulo')
		verbose_name_plural = _('Capítulos')
