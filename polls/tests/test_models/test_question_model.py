from django.test import TestCase

from polls.models import Question


class TestQuestionModel(TestCase):
    def setUp(self) -> None:
        pass

    def test_field_title(self):
        field = Question._meta.fields['title']

        self.assertEqual(field.max_length, 255)
