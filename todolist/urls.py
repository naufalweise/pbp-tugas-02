from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('create-task', views.create_task, name='create task'),
    path('logout', views.logout, name='logout')
]