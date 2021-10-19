from django.contrib import admin
from . import models


class QuestionInline(admin.StackedInline):
    model = models.Question
    extra = 0
    show_change_link = True


@admin.register(models.Quizz)
class QuizAdmin(admin.ModelAdmin):
    inlines = (
        QuestionInline,
    )

    list_display = (
        "id",
        "title",
        "start_date",
        "finish_date",
        "is_active"
    )

    readonly_fields = (
        "id",
        "start_date",
        "is_active"
    )

