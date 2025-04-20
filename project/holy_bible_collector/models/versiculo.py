# -*- coding: utf-8 -*-

from .capitulo import Capitulo
from .idioma import Idioma
from .livro_versao import LivroVersao
from django.db import models
from django.utils.translation import gettext_lazy as _


class VersiculoManager(models.Manager):
    pass


class Versiculo(models.Model):
    objects = VersiculoManager()

    id = models.BigAutoField(primery_key=True, verbose_name=_('ID'), null=False)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE, verbose_name=_('Capítulo'), null=False)
    livro_versao = models.ForeignKey(LivroVersao, on_delete=models.CASCADE, verbose_name=_('Livro/Versão'), null=False)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, verbose_name=_('Idioma'), null=False)
    texto = models.TextField(verbose_name=_('Texto do Versículo'), null=False, blank=False)
    fonte = models.CharField(max_length=2048, verbose_name=_('Fonte'), null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'))
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado Em'))

    class Meta:
        db_table = 'versiculo'
        verbose_name = _('Versículo')
        verbose_name_plural = _('Versículos')
