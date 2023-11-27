from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewTaskForm, CreateTaskForm
from django.contrib.messages import error


def home_list_view(request):
    if request.method == 'POST':
        search_query = request.POST['search']
        search = Task.objects.filter(title__contains=search_query)
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
            return redirect('detail_task_view')
    else:
        form = NewTaskForm(instance=task_instance)
    return render(request, 'task/task_done.html', {'forms': form})


@login_required
def create_task_form(request):
    if request.method == 'POST':
        task_form = CreateTaskForm(request.POST)
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.user = request.user
            task_form.save()
            return redirect('detail_task_view')
    else:
        task_form = CreateTaskForm()
    return render(request, 'task/create_task_form.html', {'form': task_form})


@login_required
def update_task_form(request, pk):
    edit_task = get_object_or_404(Task, pk=pk)
    print((edit_task, '------------------------------------------------------------------------------------------------'))

    if edit_task.user != request.user:
        error(request, 'You do not have permission to edit this task.')
        return redirect('detail_task_view')

    if request.method == 'POST':
        form = CreateTaskForm(request.POST or None, instance=edit_task)
        if form.is_valid():
            form.save()
            return redirect('detail_task_view')
    else:
        form = CreateTaskForm(instance=edit_task)
        # form = CreateTaskForm()

    return render(request, 'task/task_update.html', {'forms': form})









# def task_search(request):
#     if request.method == 'POST':
#         search_query = request.POST['search']
#         search = Task.objects.filter(title__contains=search_query)
#         print(search, '********************************************************')
#         return render(request, 'task/task_search.html', {'searchs': search})
#     else:
#         return render(request, 'task/task_search.html', {})

