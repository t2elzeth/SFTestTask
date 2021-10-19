from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title
