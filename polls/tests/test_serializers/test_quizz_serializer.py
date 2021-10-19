from django.test import TestCase

from polls.serializers import QuizzSerializer
from polls.models import Quizz


class TestQuizzSerializerMeta(TestCase):
    def setUp(self) -> None:
        self.meta = QuizzSerializer.Meta

    def test_meta_attr_model(self):
        self.assertEqual(self.meta.model, Quizz)

    def test_meta_attr_fields(self):
        expected_fields = (
            "id",
            "title",
            "start_date",
            "finish_date",
            "description"
        )
        self.assertEqual(self.meta.fields, expected_fields)