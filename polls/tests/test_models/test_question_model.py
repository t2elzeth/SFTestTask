from django.test import TestCase
from django.db import models

from polls.models import Question, Quiz
from polls.tests.factory import QuestionFactory


class TestQuestionModelFields(TestCase):
    def setUp(self) -> None:
        pass

    def get_field(self, field_name: str) -> models.Field:
        return Question._meta.get_field(field_name)

    def test_field_quiz(self):
        field_name = "quiz"
        field = self.get_field(field_name)

        self.assertIsInstance(field, models.ForeignKey)
        self.assertEqual(field.remote_field.model, Quiz)
        self.assertEqual(field.remote_field.on_delete, models.CASCADE)

    def test_field_content(self):
        field_name = "content"
        field = self.get_field(field_name)

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 255)

    def test_field_question_type(self):
        field_name = "question_type"
        field = self.get_field(field_name)

        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 30)

        # Test field choices
        self.assertEqual(Question.QUESTION_TYPE_TEXT, "text")
        self.assertEqual(Question.QUESTION_TYPE_SINGLE_CHOICE, "single_choice")
        self.assertEqual(Question.QUESTION_TYPE_MULTI_CHOICE, "multi_choice")

        self.assertEqual(
            Question.QUESTION_TYPE_CHOICES,
            ((Question.QUESTION_TYPE_TEXT, Question.QUESTION_TYPE_TEXT),
             (Question.QUESTION_TYPE_SINGLE_CHOICE, Question.QUESTION_TYPE_SINGLE_CHOICE),
             (Question.QUESTION_TYPE_MULTI_CHOICE, Question.QUESTION_TYPE_MULTI_CHOICE))
        )


class TestQuestionModelMethods(TestCase):
    def setUp(self) -> None:
        self.instance: Question = QuestionFactory.create()

    def test_string_representation(self):
        string_representation = str(self.instance)
        self.assertEqual(string_representation, self.instance.content)
