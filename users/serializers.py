from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "is_superuser",
            "is_staff",
        ]

        extra_kwargs = {"password": {"write_only": True}}

        username = serializers.CharField(
            validators=[
                UniqueValidator(
                    queryset=User.objects.all(),
                    message="A user with that username already exists",
                )
            ]
        )

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data["password"])
        new_user.save()
        return new_user
