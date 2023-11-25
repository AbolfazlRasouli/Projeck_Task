from django.shortcuts import render
from django.http import HttpResponse


def home_list_view(request):
    return render(request, 'task/home_list_view.html')

