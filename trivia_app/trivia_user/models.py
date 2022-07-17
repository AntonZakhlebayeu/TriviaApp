from datetime import datetime, timedelta

import jwt
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from trivia_app import settings


class UserManager(BaseUserManager):
    def create_user(
        self, username, email, first_name=None, last_name=None, password=None
    ):

        if email is None:
            raise TypeError("Users must have an email address.")

        if username is None:
            raise TypeError("Users must have an username")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.save()

        return user


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def access_token(self):
        return self._generate_access_jwt_token()

    def _generate_access_jwt_token(self):
        dt = datetime.now() + timedelta(hours=5)
        token = jwt.encode(
            {"id": self.pk, "exp": int(dt.strftime("%s"))},
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return token
