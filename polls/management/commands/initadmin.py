from os import getenv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    USERNAME_ENV_VAR = "DJANGO_ADMIN_USERNAME"
    PASSWORD_ENV_VAR = "DJANGO_ADMIN_PASSWORD"

    DEFAULT_USERNAMES = {
        "email": "admin@gmail.com",
        "username": "admin",
        "phone": "996312312312",
    }

    def get_default_username(self) -> str:
        default_username = self.DEFAULT_USERNAMES.get(User.USERNAME_FIELD)
        if default_username is None:
            raise ValueError("Unsupported User.USERNAME_FIELD")
        return default_username

    def get_default_password(self) -> str:
        return "admin"

    def get_username(self):
        return getenv(self.USERNAME_ENV_VAR) or self.get_default_username()

    def get_password(self):
        return getenv(self.PASSWORD_ENV_VAR) or self.get_default_password()

    def get_username_field(self):
        return User.USERNAME_FIELD

    def check_user_exists(self) -> bool:
        user_filter = {self.get_username_field(): self.get_username()}
        return User.objects.filter(**user_filter).exists()

    def get_user_data(self):
        username_field = self.get_username_field()
        username = self.get_username()
        password = self.get_password()

        user_data = {
            username_field: username,
            "password": password
        }
        if 'email' in User.REQUIRED_FIELDS and username_field != "email":
            user_data.update({'email': "admin@gmail.com"})
        return user_data

    def create_superuser(self):
        user_data = self.get_user_data()
        user = User.objects.create_superuser(**user_data)
        return user

    def handle(self, *args, **options):
        username = self.get_username()
        user_exists = self.check_user_exists()
        if not user_exists:
            self.create_superuser()
            print(f"{username} user has been created!")
        else:
            print(f"{username} user already exists!")
