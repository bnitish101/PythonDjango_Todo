from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name='api-overview'),
    path('todo-list/', views.toDoList, name='todo-list'),
    path('todo-detail/<str:pk>/', views.toDoDetail, name='todo-detail'),
    path('todo-create/', views.toDoCreate, name='todo-create'),
    path('todo-update/<str:pk>/', views.toDoUpdate, name='todo-update'),
    path('todo-delete/<str:pk>/', views.toDoDelete, name='todo-delete'),
]