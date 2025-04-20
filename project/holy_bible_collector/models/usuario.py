# -*- coding: utf-8 -*-

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UsuarioManager(models.Manager):
	pass


class Usuario(AbstractBaseUser):
	objects = UsuarioManager()