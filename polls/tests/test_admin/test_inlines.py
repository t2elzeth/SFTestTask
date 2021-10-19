from django.test import TestCase

from polls.admin import QuestionInline, QuestionChoiceInline
from polls.models import Question, QuestionChoice


class TestQuestionInline(TestCase):
    def setUp(self) -> None:
        self.inline_class = QuestionInline

    def test_field_model(self):
        self.assertEqual(self.inline_class.model, Question)

    def test_field_extra(self):
        self.assertEqual(self.inline_class.extra, 0)

    def test_field_show_change_link(self):
        self.assertTrue(self.inline_class.show_change_link)


class TestQuestionChoiceInline(TestCase):
    def setUp(self) -> None:
        self.inline_class = QuestionChoiceInline

    def test_field_model(self):
        self.assertEqual(self.inline_class.model, QuestionChoice)

    def test_field_extra(self):
        self.assertEqual(self.inline_class.extra, 0)
