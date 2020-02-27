from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(null=True)
    completed_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title