from django.db import models

# Create your models here.
class Cnab(models.Model):
    type= models.CharField(max_length=1)
    date= models.DateField()
    value= models.IntegerField()
    hour = models.TimeField()
    
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