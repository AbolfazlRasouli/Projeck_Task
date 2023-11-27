from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    hints = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}: {self.user}'




