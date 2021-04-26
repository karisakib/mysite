from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello World")

# view using loader()
# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

# view using render()
def index(request):
    return render(request, 'index.html')

def one(request):
    first_name = 'Kari'
    last_name = 'Sakib'
    return render(request, 'one.html')

def two(request):
    return render(request, 'two.html')