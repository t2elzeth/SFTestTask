from django.test import TestCase

from polls.models import Question
from django.db import models


class TestQuestionModelFields(TestCase):
    def get_field(self, field_name: str) -> models.Field:
        return Question._meta.get_field(field_name)

    def test_field_title(self):
        field = self.get_field("title")

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 255)

    def test_field_start_date(self):
        field = self.get_field("start_date")

        self.assertIsInstance(field, models.DateTimeField)

    def test_field_finish_date(self):
        field = self.get_field("finish_date")

        self.assertIsInstance(field, models.DateTimeField)
        self.assertTrue(field.auto_now_add)

    def test_field_description(self):
        field = self.get_field("description")

        self.assertIsInstance(field, models.TextField)


class TestQuestionModelMethods(TestCase):
    def setUp(self) -> None:
        self.instance = Question.objects.create(
            title="My title",
            start_date="2003-11-22 01:01:58",
            description="My question description"
        )

    def test_str(self):
        string_representation = str(self.instance)
        self.assertEqual(string_representation, "My title")
