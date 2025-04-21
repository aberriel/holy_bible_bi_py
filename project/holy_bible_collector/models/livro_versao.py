# -*- coding: utf-8 -*-

from .livro import Livro
from .versao import Versao
from django.db import models
from django.utils.translation import gettext as _
import uuid


class LivroVersaoManager(models.Manager):
    pass


class LivroVersao(models.Model):
    objects = LivroVersaoManager()

    id = models.UUIDField('Id', primary_key=True, verbose_name=_('ID'), null=False, blank=False)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name=_('Livro'), db_column='livro_id', null=False)
    versao = models.ForeignKey(Versao, on_delete=models.CASCADE, verbose_name=_('Versão'), db_column='versao_id', null=False)
    fonte = models.CharField(max_length=2048, verbose_name=_('Fonte'), null=True, blank=True)
    nome_versao = models.CharField(max_length=512, verbose_name=_('Nome do Livro na Versão'), null=True, blank=True)
    detalhes = models.TextField(verbose_name=_('Detalhes'), null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'), null=False)

    class Meta:
        db_table = 'livro_versao'
        db_table_comment = 'Relaciona os livros das Escrituras com as versões nas quais estão disponíveis'
        ordering = ['livro__nome', 'versao__nome', 'nome_versao']
        verbose_name = _('Versão do Livro')
        verbose_name_plural = _('Versões dos Livros')
