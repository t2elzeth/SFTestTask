from django.test import TestCase

from polls.admin import QuestionAdmin, QuestionChoiceInline


class TestQuestionAdmin(TestCase):
    def setUp(self) -> None:
        self.admin_class = QuestionAdmin

    def test_inlines(self):
        self.assertEqual(self.admin_class.inlines, (QuestionChoiceInline, ))