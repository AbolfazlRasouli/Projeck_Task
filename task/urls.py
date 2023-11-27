from django.urls import path, include
from .views import home_list_view, detail_view, task_done_view


urlpatterns = [
    path('', home_list_view, name='home_task_view'),
    path('detail/', detail_view, name='detail_task_view'),
    path('<int:pk>/taskdone/', task_done_view, name='create_task_done'),


]
