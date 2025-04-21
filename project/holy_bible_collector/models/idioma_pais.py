# -*- coding: utf-8 -*-

from .idioma import Idioma
from .pais import Pais
from django.db import models
from django.utils.translation import gettext_lazy as _


class IdiomaPais(models.Model):
    idioma = mdoels.ForeignKey(Idioma, on_delete=models.DO_NOTHING, db_column='idioma_id', null=False)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, db_column='pais_id', null=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    def __str__(self):
        return f'{self.pais.nome} - {self.idioma.nome}'

    class Meta:
        db_table = 'idioma_pais'
        db_table_comment = 'Relaciona países a idiomas nos quais as Escrituras foram traduzidas'
        ordering = ['pais__nome', 'idioma__nome']
