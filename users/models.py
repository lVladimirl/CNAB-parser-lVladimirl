from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from django.core import validators
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
