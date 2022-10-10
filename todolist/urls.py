from unicodedata import name
from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('create-task', views.create_task, name='create task'),
    path('logout', views.logout, name='logout'),
    path('json', views.get_task_list, name="get task list"),
    path('add', views.create_task),
    path('delete/<int:id>', views.delete, name='delete'),
    path('toggle', views.toggle_finish, name='toggle finish'),
]