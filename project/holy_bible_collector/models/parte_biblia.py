# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _


class ParteBiblia(models.TextChoices):
    ANTIGO_TESTAMENTO = 'AT', _('Antigo Testamento')
    NOVO_TESTAMENTO = 'NT', _('Novo Testamento')
