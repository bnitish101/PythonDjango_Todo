# from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework import status
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
        'Todo Create' : '/todo-create/',
        'Todo Update' : '/todo-update/<str:pk>/',
        'Todo Delete' : '/todo-delete/<str:pk>/',
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

@api_view(['POST'])
def toDoCreate(request):
    if request.method == 'POST':
        serializer = ToDoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def toDoUpdate(request, pk):
    if request.method == 'POST':
        todo_detail = ToDo.objects.get(pk=pk)
        # serializer = ToDoSerializer(instance=todo_detail, data=request.data) # this will work fine with instance
        serializer = ToDoSerializer(todo_detail, data=request.data) # this will work fine without instance too, refernce from official document (https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def toDoDelete(request, pk):
    if request.method == 'DELETE':
        todo_detail = ToDo.objects.get(pk=pk)
        todo_detail.delete()
        return Response('Deleted Successfully!', status=status.HTTP_204_NO_CONTENT)
        # return Response('Deleted Successfully!')
        