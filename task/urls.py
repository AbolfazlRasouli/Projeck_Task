from django.urls import path, include
from .views import home_list_view, detail_view, task_done_view, create_task_form, update_task_form, task_search, task_delete


urlpatterns = [
    path('', home_list_view, name='home_task_view'),
    path('detail/', detail_view, name='detail_task_view'),
    path('<int:pk>/taskdone/', task_done_view, name='create_task_done'),
    path('new/', create_task_form, name='create_task_form'),
    path('<int:pk>/edit_task_form/', update_task_form, name='update_task_form'),
    path('search/', task_search, name='task_search'),
    path('<int:pk>/delete/', task_delete, name='task_delete'),
]
