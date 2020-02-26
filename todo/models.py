from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    completed_at = models.DateField()

    def __str__(self):
        return self.title