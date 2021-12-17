from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)
    tasks = models.CharField(max_length=70)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.tasks
