from django.urls import path
from . import views
urlpatterns = [
    path('todolist/', views.todo_list,name='todolist'),
    path('', views.todo_creation,name='todo_create'),
    path('<int:id>/', views.todo_creation,name='todo_update'),
    path('tododelete/<int:id>', views.todo_delete,name='todo_delete'),
    path('login',views.todo_login,name='todo_login'),
    path('signup',views.todo_signup,name='todo_signup'),
    path('profile',views.todo_profile,name='profile')
]
