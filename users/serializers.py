from rest_framework import serializers

from users.models import User

# from animes.serializers import AnimeSerializer

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "cpf",
            # "card",
            "username",
        ]

        read_only_fields=[
            "id"
        ]

        extra_kwargs={
            # "card":{"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "username","cpf"]

class UserRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "username","cpf"]