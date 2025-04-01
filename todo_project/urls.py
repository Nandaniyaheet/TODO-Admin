"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import todo_list, create_todo, update_todo, delete_todo, important_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todo_list'), 
    path('create/', create_todo, name='create_todo'),
    path('update/<int:todo_id>/', update_todo, name='update_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('important/<int:todo_id>/', important_todo, name='important_todo'),
]
