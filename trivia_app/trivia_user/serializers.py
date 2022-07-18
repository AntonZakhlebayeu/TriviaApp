from django.contrib.auth import authenticate
from rest_framework import serializers
from trivia_user.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = [
            "pk",
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
            "access_token",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.SlugField(max_length=128, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
            "access_token",
        ]

    def validate(self, data):
        email = data.get(
            "email",
        )
        password = data.get(
            "password",
        )

        if email is None:
            raise serializers.ValidationError(
                "An email address is required to log in."
            )

        if password is None:
            raise serializers.ValidationError(
                "A password is required to log in."
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password was not found."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "This user has been deactivated."
            )

        return {
            "id": user.pk,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "access_token": user.access_token,
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
            "is_active",
            "is_staff",
        ]
        read_only_fields = [
            "is_active",
            "is_staff",
        ]

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
