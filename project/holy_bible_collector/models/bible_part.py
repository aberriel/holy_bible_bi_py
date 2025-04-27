# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext as _


class BiblePart(models.TextChoices):
    OLD_TESTAMENT = 'OT', _('Old Testamento')
    NEW_TESTAMENT = 'NT', _('New Testamento')
