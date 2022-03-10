from django.urls import path
from . import views

urlpatterns = [
    path('todo-list', views.toDoList, name='todo-list'),
]