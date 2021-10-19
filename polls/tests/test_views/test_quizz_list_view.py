from django.test import TestCase
from polls.views import QuizzListAPIView
from polls.serializers import QuizzSerializer


# from polls.models import Quizz
# from django.utils import timezone


class TestQuizListAPIView(TestCase):
    def setUp(self) -> None:
        self.view_class = QuizzListAPIView

    def test_attr_serializer_class(self):
        self.assertEqual(self.view_class.serializer_class, QuizzSerializer)

    def test_get_queryset_method(self):
        # TODO: Write test for get_queryset() method
        pass
