# -*- coding: utf-8 -*-

from .country import Country
from .language import Language
from django.db import models
from django.utils.translation import gettext_lazy as _


class LanguageCountry(models.Model):
    language = mdoels.ForeignKey(Language, on_delete=models.DO_NOTHING, db_column='language_id', null=False)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, db_column='country_id', null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado Em'), null=False)

    def __str__(self):
        return f'{self.country.name} - {self.language.name}'

    class Meta:
        db_table = 'language_country'
        db_table_comment = 'Relaciona países a idiomas nos quais as Escrituras foram traduzidas'
        ordering = ['country__name', 'language__name']
