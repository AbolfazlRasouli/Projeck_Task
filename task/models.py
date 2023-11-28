from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.upper()


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    date_deadline = models.DateField()
    time_deadline = models.TimeField()
    status = models.BooleanField(default=False)
    user_Constructive = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks_Constructive')
    user_doing = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks_doing')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    hints = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title.upper()}'




