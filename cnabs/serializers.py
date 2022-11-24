from rest_framework import serializers

from .models import Cnab

class CnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields= "__all__"
        ready_only_fields = ["id"]