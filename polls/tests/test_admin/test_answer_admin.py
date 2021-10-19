from django.test import TestCase
from polls.admin import AnswerAdmin


class TestAnswerAdmin(TestCase):
    def setUp(self) -> None:
        self.admin_class = AnswerAdmin
