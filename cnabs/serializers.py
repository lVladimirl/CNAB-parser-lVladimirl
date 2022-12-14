from rest_framework import serializers

from .models import Cnab
from users.serializers import UserSerializer
from shops.serializers import ShopViewSerializer
class CnabSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cnab
        fields= ['type','date','value','hour','card']
        ready_only_fields = ["id"]
        
class CnabViewSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    shop = ShopViewSerializer()
    class Meta:
        model = Cnab
        fields= ['type','date','value','hour','card','owner','shop']
        ready_only_fields = ["id","shop","owner"]