from django.urls import path, include
from .views import home_list_view


urlpatterns = [
    path('', home_list_view, name='home_list_view')
]
