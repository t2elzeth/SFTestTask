from rest_framework import serializers

from polls import models


class QuizzSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quizz
        fields = (
            "id",
            "title",
            "start_date",
            "finish_date",
            "description"
        )
