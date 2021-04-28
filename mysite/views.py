from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# view using render()
def index(request):
    return render(request, 'index.html')

def skills(request):
    return render(request, 'skills.html')

def experience(request):
    return render(request, 'experience.html')

def hobbies(request):
    return render(request, 'hobbies.html')