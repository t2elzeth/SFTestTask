from django.test import TestCase
from django.db import models
from polls.models import QuestionChoice, Question
from polls.tests.factory import QuestionChoiceFactory


class TestQuestionChoiceModelFields(TestCase):
    def setUp(self) -> None:
        pass

    def get_field(self, field_name) -> models.Field:
        return QuestionChoice._meta.get_field(field_name)

    def test_question_field(self):
        field_name = "question"
        field = self.get_field(field_name)

        self.assertIsInstance(field, models.ForeignKey)
        self.assertEqual(field.remote_field.model, Question)
        self.assertEqual(field.remote_field.on_delete, models.CASCADE)
        self.assertEqual(field.remote_field.related_name, "choices")

    def test_content_field(self):
        field_name = "content"
        field = self.get_field(field_name)

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 255)


class TestQuestionChoiceModelMethods(TestCase):
    def setUp(self) -> None:
        self.instance: QuestionChoice = QuestionChoiceFactory.create()

    def test_string_representation(self):
        string_representation = str(self.instance)
        self.assertEqual(string_representation, self.instance.content)
