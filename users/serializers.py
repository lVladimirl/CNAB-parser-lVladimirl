from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ["name","cpf","card"]
        ready_only_fields = ["id"]