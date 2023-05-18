from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "email", "password")

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        validated_data.pop("password")
        instance = super().update(instance, validated_data)
        return instance
