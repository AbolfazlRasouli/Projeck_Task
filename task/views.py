from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewTaskForm



def home_list_view(request):
    if request.method == 'POST':
        search_query = request.POST['search']
        search = Task.objects.filter(title__contains=search_query)
        print(search, '********************************************************')
        return render(request, 'task/task_search.html', {'searchs': search})
    else:

        # task_list = Task.objects.select_related('tasks')
        task_list = Task.objects.all()

        return render(request, 'task/home_list_view.html', {'task_list': task_list})


@login_required
def detail_view(request):
    tag = request.user
    task_detail = Task.objects.filter(user=tag)
    return render(request, 'task/detail.html', {'task_detail': task_detail})


def task_done_view(request, pk):
    task_instance = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = NewTaskForm(request.POST, instance=task_instance)
        if form.is_valid():
            form.save()
            return redirect('detail_view')
    else:
        form = NewTaskForm()
    return render(request, 'task/task_done.html', {'forms': form})


# def task_search(request):
#     if request.method == 'POST':
#         search_query = request.POST['search']
#         search = Task.objects.filter(title__contains=search_query)
#         print(search, '********************************************************')
#         return render(request, 'task/task_search.html', {'searchs': search})
#     else:
#         return render(request, 'task/task_search.html', {})

