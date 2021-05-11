"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings #
from django.conf.urls.static import static #
# import the views.py file from the same folder
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url path to our view in views.py
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('skills.html', views.skills, name='skills'),
    path('experience.html', views.experience, name='experience'),
    path('hobbies.html', views.hobbies, name='hobbies'),
    # path('db.html', views.db, name='db'),
    path('contact.html', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #
