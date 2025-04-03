from django.db import models
from list_app.models import List, BaseTemplate
# Create your models here.

class TaskTemplate(BaseTemplate):
    # name
    # completed
    description = models.TextField()

    class Meta:
        abstract = True

class Task(TaskTemplate):
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
