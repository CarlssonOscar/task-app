from django.db import models


class Task(models.Model):
    tasks = models.CharField(max_length=45)
    #Add date
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.tasks
