from rest_framework import serializers

from users.models import User

# from animes.serializers import AnimeSerializer

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "password",
            "username",
            "cpf",
            "card"
        ]

        read_only_fields=[
            "id"
        ]

        extra_kwargs={
            "password":{"write_only": True},
            "card":{"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "username","cpf","card"]

class UserRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "username","cpf"]
        