import factory

from polls.models import Question, QuestionChoice


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    content = factory.Faker("sentence", nb_words=5)
    question_type = Question.QUESTION_TYPE_TEXT


class QuestionChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QuestionChoice

    question = factory.SubFactory(QuestionFactory)
    content = factory.Faker("sentence", nb_words=3)
