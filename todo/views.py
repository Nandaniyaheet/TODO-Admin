from django.shortcuts import render, redirect,get_object_or_404
from .models import TodoModel

def todo_list(request):
    if request.GET.get("filter") == "important":
        todos = TodoModel.objects.filter(important=True).order_by('-last_modified')
    else:
        todos = TodoModel.objects.all().order_by('-last_modified')
    return render(request, 'todo/todo_list.html',{'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed')== 'on'
        TodoModel.objects.create(title=title, description=description, completed=completed)
        return redirect('todo_list')
    return render(request, 'todo/create_todo.html')

def update_todo(request, todo_id):
    todo = TodoModel.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed') == 'on' 
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/update_todo.html', {'todo':todo})

def delete_todo(request, todo_id):
    todo = TodoModel.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    
def important_todo(request, todo_id):
    todo = TodoModel.objects.get(id=todo_id)
    todo.important = not todo.important
    todo.save()
    return redirect('todo_list')