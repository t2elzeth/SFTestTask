from django.db import models
from django.utils import timezone


class Quizz(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def is_active(self) -> bool:
        if self.id is None:
            return False
        return timezone.now() < self.finish_date

    class Meta:
        verbose_name = "Quizz"
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    quiz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    QUESTION_TYPE_TEXT = "text"
    QUESTION_TYPE_SINGLE_CHOICE = "single_choice"
    QUESTION_TYPE_MULTI_CHOICE = "multi_choice"
    QUESTION_TYPE_CHOICES = ((QUESTION_TYPE_TEXT, QUESTION_TYPE_TEXT),
                             (QUESTION_TYPE_SINGLE_CHOICE, QUESTION_TYPE_SINGLE_CHOICE),
                             (QUESTION_TYPE_MULTI_CHOICE, QUESTION_TYPE_MULTI_CHOICE))
    question_type = models.CharField(max_length=30, choices=QUESTION_TYPE_CHOICES)

    def __str__(self):
        return self.content


class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


class Answer(models.Model):
    user_id = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices = models.ManyToManyField(QuestionChoice)

    def __str__(self):
        # TODO: Test string representation
        return f"{self.user_id}"
