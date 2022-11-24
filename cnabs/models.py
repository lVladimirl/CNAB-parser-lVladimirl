from django.db import models

from django.db import models

# class Cnab(models.Model):
#     type= models.CharField(max_length=1)
#     date= models.DateField()
#     value= models.IntegerField()
#     cpf= models.CharField(max_length=11)
#     card = models.CharField(max_length=12)
#     hour = models.TimeField()
#     owner = models.CharField(max_length=14)
#     shop = models.CharField(max_length=19)

class Cnab(models.Model):
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