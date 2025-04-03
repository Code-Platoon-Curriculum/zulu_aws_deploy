from django.db import models
from user_app.models import App_user

# Create your models here.
class BaseTemplate(models.Model):
    name = models.CharField()
    completed = models.BooleanField(default=False)

    class Meta:
        abstract = True

class List(BaseTemplate):
    user = models.ForeignKey(App_user, on_delete=models.CASCADE, related_name='lists')
