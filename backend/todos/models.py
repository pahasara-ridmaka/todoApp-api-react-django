from django.db import models

class Todo(models.Model):
    title = models.TextField(max_length=200)
    body = models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.title
