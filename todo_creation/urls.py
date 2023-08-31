from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('todolist/', views.todo_list,name='todolist'),
    path('', views.todo_creation,name='todo_create'),
    path('<int:id>/', views.todo_creation,name='todo_update'),
    path('tododelete/<int:id>', views.todo_delete,name='todo_delete'),
]
