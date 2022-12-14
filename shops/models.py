import uuid

from django.db import models

class Shop(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="shops"
        )