from django.test import TestCase

from polls.admin import QuizzAdmin
from polls.admin import QuestionInline


class TestQuizzAdmin(TestCase):
    def setUp(self) -> None:
        self.admin_class = QuizzAdmin

    def test_inlines(self):
        self.assertIsInstance(self.admin_class.inlines, tuple)
        self.assertEqual(self.admin_class.inlines, (QuestionInline,))

    def test_list_display(self):
        self.assertIsInstance(self.admin_class.list_display, tuple)
        self.assertEqual(self.admin_class.list_display, (
            "id",
            "title",
            "start_date",
            "finish_date",
            "is_active"
        ))

    def test_readonly_fields(self):
        self.assertIsInstance(self.admin_class.readonly_fields, tuple)
        self.assertEqual(self.admin_class.readonly_fields, (
            "id",
            "start_date",
            "is_active"
        ))
