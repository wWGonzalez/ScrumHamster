"""scrum : data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from .views import index
from .views import list_client, create_client
from .views import list_project, create_project
from .views import list_requirement, create_requirement
from .views import list_homework, create_homework
from .views import list_mistakes, create_mistakes
from .views import list_comments, create_comments
from .views import list_rol, create_rol

urlpatterns = [
    path('', index, name = 'index'),

    path('list_client', list_client, name = 'list_client'),
    path('create_client', create_client, name = 'create_client'),

    path('list_project', list_project, name = 'list_project'),
    path('create_project', create_project, name = 'create_project'),

    path('list_requirement', list_requirement, name = 'list_requirement'),
    path('create_requirement', create_requirement, name = 'create_requirement'),

    path('list_homework', list_homework, name = 'list_homework'),
    path('create_homework', create_homework, name = 'create_homework'),

    path('list_mistakes', list_mistakes, name = 'list_mistakes'),
    path('create_mistakes', create_mistakes, name = 'create_mistakes'),

    path('list_comments', list_comments, name = 'list_comments'),
    path('create_comments', create_comments, name = 'create_comments'),

    path('list_rol', list_rol, name = 'list_rol'),
    path('create_rol', create_rol, name = 'create_rol'),
]