# -*- coding: utf-8 -*-

from .versao import Versao
from django.db import models
from django.utils.translation import gettext as _
import uuid


class LivroManager(models.Manager):
    def get_by_id(self, livro_id):
        queryset = self.get_queryset()
        livro = queryset.get(id=livro_id)
        return livro


class Livro(models.Model):
    objects = LivroManager()

    id = models.UUIDField(primary_key=True, verbose_name=_('ID'), null=False, default=uuid.uuid4)
    nome = models.CharField(max_length=128, verbose_name=_('Nome'), null=False)
    autor = models.ForeignKey(Autor, verbose_name=_('Autor'), on_delete=models.SET_NULL, db_column='autor_id', null=True)
    ano_estimado_escrita = models.CharField(max_length=9, verbose_name=_('Ano estimado da escrita'), null=True, blank=True)
    idioma_original = models.ForeignKey(Idioma, verbose_name=_('Idioma'), on_delete=models.CASCADE, db_column='idioma_id', null=True)
    apocrifo = models.BooleanField(verbose_name=_('É apócrifo?'), default=False, null=False)
    descricao = models.TextField(verbose_name=_('Descrição'), null=True)
    detalhes = models.TextField(verbose_name=_('Detalhes'), null=True)
    parte_biblia = models.CharField(max_length=2, choices=ParteBiblia, verbose_name=_('Parte das Escrituras'), db_column='parte_biblia', null=False, blank=False)
    versoes = models.ManyToManyField(Versao, through='LivroVersao')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'livro'
        db_table_comment = 'Livros das Escrituras'
        # uniquetogether = (('parte_biblia', 'nome'))
        ordering = ['parte_biblia', 'nome']
        verbose_name = _('Livro')
        verbose_name_plural = _('Livros')
        constraints = [
            models.UniqueConstraint(name='unique_parte_nome', fields=['parte_biblia', 'nome'], null_distinct=True)
        ]
