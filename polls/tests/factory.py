import factory

from polls.models import Question, QuestionChoice, Quizz
from django.utils import timezone
from datetime import timedelta


class QuizzFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quizz

    title = factory.Faker("sentence", nb_words=3)
    finish_date = factory.LazyFunction(lambda: timezone.now() + timedelta(days=2))
    description = factory.Faker("paragraph", nb_sentences=3)


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    quiz = factory.SubFactory(QuizzFactory)
    content = factory.Faker("sentence", nb_words=5)
    question_type = Question.QUESTION_TYPE_TEXT


class QuestionChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QuestionChoice

    question = factory.SubFactory(QuestionFactory)
    content = factory.Faker("sentence", nb_words=3)
