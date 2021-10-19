from django.test import TestCase
from django.db import models
from polls.models import Answer, QuestionChoice, Question


class TestAnswerModelFields(TestCase):
    def get_field(self, field_name: str) -> models.Field:
        return Answer._meta.get_field(field_name)

    def test_field_user_id(self):
        field_name = "user_id"
        field = self.get_field(field_name)

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 255)

    def test_field_question(self):
        field_name = "question"
        field = self.get_field(field_name)

        self.assertIsInstance(field, models.ForeignKey)
        self.assertEqual(field.remote_field.model, Question)
        self.assertEqual(field.remote_field.on_delete, models.CASCADE)

    def test_field_choices(self):
        field_name = "choices"
        field = self.get_field(field_name)

        self.assertIsInstance(field, models.ManyToManyField)
        self.assertEqual(field.remote_field.model, QuestionChoice)
