from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib import messages
# Create your views here.

@login_required
def tasklist(request):
    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search)

    else:

        tasks_list = Task.objects.all().order_by('-created_at')

        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'Doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def edittask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'task': task, 'form': form})

    else:
        return render(request, 'tasks/edittask.html', {'task': task, 'form': form})

@login_required
def deletetask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('/')