from django.shortcuts import render

# Create your views here.
def toDoList(request):
    context = {}
    return render(request, 'frontend/todo-list.html', context)