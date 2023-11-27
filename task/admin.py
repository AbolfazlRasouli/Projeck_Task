from django.contrib import admin
from .models import Category, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_time', 'status', 'user',)


admin.site.register(Category)
