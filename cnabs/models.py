from django.db import models

from django.db import models

import uuid

class Cnab(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type= models.CharField(max_length=1)
    date= models.DateField()
    value= models.IntegerField()
    hour = models.TimeField()
    card = models.CharField(max_length=12)
    
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="transactions"
        )
    shop = models.ForeignKey(
        "shops.Shop",
        on_delete=models.CASCADE,
        related_name="transactions"
        )