from rest_framework import generics
from django.utils import timezone
from . import serializers, models


class QuizzListAPIView(generics.ListAPIView):
    serializer_class = serializers.QuizzSerializer

    def get_queryset(self):
        return models.Quizz.objects.filter(finish_date__lt=timezone.now())
