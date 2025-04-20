# -*- coding: utf-8 -*-

from .versao import Versao
from django.db import models
from django.utils.translation import gettext as _


class LivroManager(models.Manager):
    def get_by_id(self, livro_id):
        queryset = self.get_queryset()
        livro = queryset.get(id=livro_id)
        return livro


class Livro(models.Model):
    objects = LivroManager()

    id = models.BigAutoField(primary_key=True, verbose_name=_('ID'), null=False)
    nome = models.CharField()
    autor = models.ForeignKey()
    ano_estimado_escrita = models.CharField()
    idioma_original = models.ForeignKey()
    apocrifo = models.BooleanField(verbose_name=_('É apócrifo?'), default=False, null=False)
    descricao = models.TextField(verbose_name=_('Descrição'), null=True)
    detalhes = models.TextField(verbose_name=_('Detalhes'), null=True)
    parte_biblia = mo
    versoes = models.ManyToManyField(Versao, through='LivroVersao')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'livro'
        verbose_name = _('Livro')
        verbose_name_plural = _('Livros')
