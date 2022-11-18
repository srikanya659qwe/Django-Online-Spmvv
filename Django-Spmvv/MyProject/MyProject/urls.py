"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from MyApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hai,name='hi'),
    path('hello/',views.hello,name='hello'),

    path('dyn/<int:id>/',views.dynamic,name='dyn'),
    path('data/<str:name>/',views.data,name='data'),
    path('task/<int:a>/<str:b>/',views.task,name='task'),


    path('temp/',views.temp,name='temp'),
    path('table/',views.table,name='table'),
    path('get/<int:n>/<str:m>/',views.get,name='get'),


    path('inline/',views.inline,name='inline'),
    path('internal/',views.internal,name='internal'),
    path('external/',views.external,name='external')


]
