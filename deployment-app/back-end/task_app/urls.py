from django.urls import path
from .views import All_tasks

urlpatterns = [
    path("", All_tasks.as_view()),
]