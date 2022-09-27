from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from .models import Task

# Create your views here.
def index(request):
	task_list = Task.objects.all()
	context = {'task_list': task_list}
	return (request, 'index.html', context)

def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Akun telah berhasil dibuat!')
			return redirect('wishlist:login')
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

