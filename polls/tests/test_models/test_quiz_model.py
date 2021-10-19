from django.test import TestCase

from polls.models import Quizz
from django.db import models
from django.utils import timezone
from datetime import timedelta


class TestQuizModelFields(TestCase):
    def get_field(self, field_name: str) -> models.Field:
        return Quizz._meta.get_field(field_name)

    def test_field_title(self):
        field = self.get_field("title")

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 255)

    def test_field_start_date(self):
        field = self.get_field("start_date")

        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.auto_now_add)

    def test_field_finish_date(self):
        field = self.get_field("finish_date")

        self.assertIsInstance(field, models.DateTimeField)

    def test_field_description(self):
        field = self.get_field("description")

        self.assertIsInstance(field, models.TextField)


class TestQuizModelMethods(TestCase):
    def setUp(self) -> None:
        self.instance = Quizz.objects.create(
            title="My title",
            finish_date=timezone.now() - timedelta(days=2),
            description="My quiz description"
        )

    def test_string_representation(self):
        string_representation = str(self.instance)
        self.assertEqual(string_representation, "My title")

    def test_is_active(self):
        self.assertFalse(self.instance.is_active)

        self.instance.finish_date = timezone.now() + timedelta(days=2)
        self.instance.save()
        self.assertTrue(self.instance.is_active)


class TestQuizModelMeta(TestCase):
    def setUp(self) -> None:
        self.meta = Quizz._meta

    def test_verbose_name(self):
        self.assertEqual(self.meta.verbose_name, "Quizz")

    def test_verbose_name_plural(self):
        self.assertEqual(self.meta.verbose_name_plural, "Quizzes")
