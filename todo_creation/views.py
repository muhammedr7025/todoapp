from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
# Create your views here.
@login_required(login_url='/login')
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
            form=TodoForm(request.POST)
            userid=request.user.id
            form.user=userid
            print(form.data)
            print(form)
            
        else:
            todo=Todo.objects.get(pk=id)
            form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            print('formsaved')
        return redirect('todolist')
@login_required(login_url='/login')
def todo_list(request):
    today = datetime.date.today()
    outdate=Todo.objects.filter(user=request.user.id, date__lt=today)
    print(outdate)
    context={'todolist':Todo.objects.filter(user=request.user.id),'outdate':outdate}
    return render(request,'todo_list.html',context)
@login_required(login_url='/login')
def todo_delete(request,id):
    todo=Todo.objects.get(pk=id)
    todo.delete()
    return redirect('todolist')

def todo_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            print(user)
            auth.login(request,user)
            return redirect('todolist')
        else:
            return render(request,'login.html',{'error':'Username or password is incorrect!'})

def todo_signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        try:
            User.objects.get(username=request.POST['username'])
            return render(request,'signup.html',{'error':'Username is already taken!'})
        except User.DoesNotExist:
            user=User.objects.create_user(request.POST['username'],password=request.POST['password'])
            auth.login(request,user)
            return redirect('todolist')

@login_required(login_url='/login')
def todo_profile(request):
    return render(request,'profile.html')
def todo_logout(request):
     logout(request)
     return redirect("todo_login")