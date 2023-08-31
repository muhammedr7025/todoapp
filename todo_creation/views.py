from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import Todo
# Create your views here.
def todo_creation(request,id=0):
    if request.method == "GET":
        if id==0:
            form=TodoForm()
        else:
            todo=Todo.objects.get(pk=id)
            form=TodoForm(instance=todo)
        return render(request,'todo_form.html',{'form':form})
    else:
        if id==0:
            print('haii')
            form=TodoForm(request.POST)
            print(request.POST)
        else:
            todo=Todo.objects.get(pk=id)
            form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('todolist')

def todo_list(request):
    context={'todolist':Todo.objects.all()}
    return render(request,'todo_list.html',context)

def todo_delete(request,id):
    todo=Todo.objects.get(pk=id)
    todo.delete()
    return redirect('todolist')
