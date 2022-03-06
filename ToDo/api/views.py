# from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import ToDo
from api.serializers import ToDoSerializer

# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'ToDo List' : 'todo-list/',
        'Todo Detail' : '/todo-detail/<str:pk>/',
        'Create Todo' : '/create-todo/',
        'Update Todo' : '/update-todo/<str:pk>/',
        'Delete Todo' : '/delete-todo/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def toDoList(request):
    todo = ToDo.objects.all()
    serializer = ToDoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toDoDetail(request, pk):
    todo_detail = ToDo.objects.get(pk=pk)
    serializer = ToDoSerializer(todo_detail, many=False)
    return Response(serializer.data)