from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Task, Tag
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewTaskForm, CreateTaskForm
from django.contrib.messages import error
from django.db.models import Q, F


def home_list_view(request):
        # task_list = Task.objects.all()
        task_list = Task.objects.select_related('user_doing').all()
        return render(request, 'task/home_list_view.html', {'task_list': task_list})


def task_search(request):
    search_query = request.GET.get('search')
    search = Task.objects.filter(Q(title__icontains=search_query) | Q(tags__name__icontains=search_query))
    return render(request, 'task/task_search.html', {'searchs': search})


@login_required
def detail_view(request):
    tag = request.user
    task_detail = Task.objects.filter(user_doing=tag)
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
    print(request.user, '=' * 50)
    if request.method == 'POST':
        task_form = CreateTaskForm(request.POST)
        if task_form.is_valid():
            # print()
            # task_form.user_Constructive = request.user
            # task_form.user_doing = request.user
            # name = task_form.cleaned_data.get('name')
            # task_form.tags = name
            new_task = task_form.save(commit=False)
            print('=' * 50, new_task, '=' * 50)
            # task_form.save()
            new_task.user_Constructive = request.user
            new_task.user_doing = request.user
            task_form.save()

            name = task_form.cleaned_data['name']
            # Tag.objects.create(name=name)

            tag, created = Tag.objects.get_or_create(name=name)
            print(tag, created)
            # Add the tag to the task
            new_task.tags.add(tag)

            # task_form.tags.add(name)




            return redirect('detail_task_view')
    else:
        task_form = CreateTaskForm()
    return render(request, 'task/create_task_form.html', {'form': task_form})


@login_required
def update_task_form(request, pk):
    edit_task = get_object_or_404(Task, pk=pk, user_Constructive=request.user)

    # if edit_task.user_Constructive != request.user:
    #     error(request, 'You do not have permission to edit this task.')
    #     return redirect('detail_task_view')

    if request.method == 'POST':
        form = CreateTaskForm(request.POST or None, instance=edit_task)
        if form.is_valid():
            form.save()
            return redirect('detail_task_view')
    else:
        form = CreateTaskForm(instance=edit_task)
    return render(request, 'task/task_update.html', {'forms': form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user_Constructive=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('detail_task_view')

    return render(request, 'task/task_delet.html', {'tasks': task})








