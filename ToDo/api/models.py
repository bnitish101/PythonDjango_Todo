from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
       return self.title 