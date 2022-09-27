from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'todolist.html', context)


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('todolist:index')
        else:
            messages.info(request, 'Username atau password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('todolist:login')


@login_required(login_url='/todolist/login')
def create_task(request):
    if request.method == 'POST':
        # buat task baru
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task(
                title=form.cleaned_data['title'], description=form.cleaned_data['description'], user=request.user, date=date.today())
            new_task.save()
            messages.success(request, 'Berhasil membuat task')
            return redirect('todolist:index')
    form = TaskForm()
    context = {'form': form}
    return render(request, 'create-task.html', context)
