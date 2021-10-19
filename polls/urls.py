from django.urls import path

from . import views

urlpatterns = (
    path("", views.QuizzListAPIView.as_view()),
)
