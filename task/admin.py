from django.contrib import admin
from .models import Category, Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime_created', 'date_deadline', 'status', 'user_Constructive', 'user_doing')


admin.site.register(Category)
admin.site.register(Tag)
