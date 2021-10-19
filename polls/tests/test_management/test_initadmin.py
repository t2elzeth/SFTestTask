from django.test import TestCase
from django.contrib.auth.models import User

from polls.management.commands import initadmin
from test.support import EnvironmentVarGuard
import faker


class TestInitAdminCommandDefaultUsernames(TestCase):
    def get_default(self, username_field: str) -> str:
        return initadmin.USER_DEFAULT_USERNAMES[username_field]

    def test_default_email_username(self):
        username_field = "email"
        username = self.get_default(username_field)
        self.assertEqual(username, "admin@gmail.com")

    def test_default_username_username(self):
        username_field = "username"
        username = self.get_default(username_field)
        self.assertEqual(username, "admin")

    def test_default_phone_username(self):
        username_field = "phone"
        username = self.get_default(username_field)
        self.assertEqual(username, "996312312312")


class TestInitAdminCommandEnvironmentVariableNames(TestCase):
    def setUp(self) -> None:
        self.command_class = initadmin.Command

    def test_username_env_var(self):
        self.assertEqual(self.command_class.USERNAME_ENV_VAR, "DJANGO_ADMIN_USERNAME")

    def test_password_env_var(self):
        self.assertEqual(self.command_class.PASSWORD_ENV_VAR, "DJANGO_ADMIN_PASSWORD")


class TestInitAdminCommandMethods(TestCase):
    def setUp(self) -> None:
        self.command = initadmin.Command()
        self.env = EnvironmentVarGuard()
        self.fake = faker.Faker()
        User.USERNAME_FIELD = "username"

    def test_get_default_username_method(self):
        User.USERNAME_FIELD = "email"
        username = self.command.get_default_username()
        self.assertEqual(username, "admin@gmail.com")

        User.USERNAME_FIELD = "username"
        username = self.command.get_default_username()
        self.assertEqual(username, "admin")

        User.USERNAME_FIELD = "phone"
        username = self.command.get_default_username()
        self.assertEqual(username, "996312312312")

        User.USERNAME_FIELD = self.fake.bothify("####")
        self.assertRaises(ValueError, self.command.get_default_username)

    def test_get_default_password_method(self):
        password = self.command.get_default_password()
        self.assertEqual(password, "admin")

    def test_get_username_method(self):
        username = self.command.get_username()
        self.assertEqual(username, self.command.get_default_username())

        self.env.set(self.command.USERNAME_ENV_VAR, "admin@gmail.com")
        with self.env:
            username = self.command.get_username()
            self.assertEqual(username, "admin@gmail.com")

    def test_get_password_method(self):
        password = self.command.get_password()
        self.assertEqual(password, self.command.get_default_password())

        env_password = self.fake.bothify("???_###*!##")
        self.env.set(self.command.PASSWORD_ENV_VAR, env_password)
        with self.env:
            password = self.command.get_password()
            self.assertEqual(password, env_password)

    def test_get_username_field_method(self):
        User.USERNAME_FIELD = "email"
        username_field = self.command.get_username_field()
        self.assertEqual(username_field, "email")

        new_username_field = self.fake.bothify("#####")
        User.USERNAME_FIELD = new_username_field
        username_field = self.command.get_username_field()
        self.assertEqual(username_field, new_username_field)

    def test_check_user_exists_method(self):
        user_exists = self.command.check_user_exists()
        self.assertFalse(user_exists)

        self.command.create_superuser()
        user_exists = self.command.check_user_exists()
        self.assertTrue(user_exists)

    def test_get_user_data_method(self):
        User.USERNAME_FIELD = "username"
        User.REQUIRED_FIELDS = ["email"]
        user_data = self.command.get_user_data()
        expected = {
            self.command.get_username_field(): self.command.get_username(),
            "password": self.command.get_password(),
            "email": "admin@gmail.com"
        }
        self.assertEqual(user_data, expected)

        User.USERNAME_FIELD = "email"
        user_data = self.command.get_user_data()
        expected = {
            self.command.get_username_field(): self.command.get_username(),
            "password": self.command.get_password()
        }
        self.assertEqual(user_data, expected)

    def test_create_superuser_method(self):
        user = self.command.create_superuser()
        self.assertIsInstance(user, User)
