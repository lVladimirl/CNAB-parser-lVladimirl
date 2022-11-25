from rest_framework import serializers

from .models import Shop
from users.serializers import UserSerializer

class RegisterShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields= ["id","name"]
        ready_only_fields = ["id"]

class ShopViewSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Shop
        fields= ["name","owner"]
        ready_only_fields = ["id","owner"]