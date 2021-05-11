from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# from mysite.models import Car, Stats

from django.contrib.auth.models import User

from .forms import UserForm, ContactForm

from .models import Contact

# from .admin inport ExampleModelForm()
# from .forms import NameForm

# view using render()
# def index(request):
#     name = 'Kari Sakib'
#     context = {
#         'name' : name
#     }
#     return render(request, 'index.html', context)

# def index(request):
#     # we can grab rows from any table
#     if request.method == 'GET':
#         form = ExampleModelForm()
#     else:
#         # binds POST request data to our form
#         form = ExampleModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, 'index.html', context={'users': users, 'form': form})

def skills(request):
    skills_list = ['Python', 'NumPy', 'Pandas', 'SciPy', 'Matplotlib', 'Seaborn', 
    'Data Visualization', 'Data Cleaning', 'Data Manipulation', 'Probability Statistics',
    'RStudio', 'SQL', 'HTML-CSS-JavaScript', 'React', 'Java']
    context = {
        'skills_list' : skills_list
    }
    return render(request, 'skills.html', context)

def experience(request):
    exp_dict = {'position': 'Data Science Fellow, Innovation Fellowship, TKH',
    'date': '09/2020 – present',
    'bullets': {
        'Enhance tech skills in Python and Data Science by participating in a competitive, project-based 9- month fellowship with 100+ hours of technology and professional development instruction.',
        'Collaborate with TKH staff and 40+ fellows in order to deliver virtual presentations of final projects to tech professionals, funders, and community stakeholders.',
        'Receive one on one mentoring with industry professionals and improve upon career development and project management skills.'
        }
    }
    context = {
        'exp_dict' : exp_dict
    }
    return render(request, 'experience.html', context)

def hobbies(request):
    return render(request, 'hobbies.html')

def db(request):
    cars = Car.objects.all()
    stats = Stats.objects.all()
    context = {
        'cars' : cars,
        'stats' : stats
    }
    return render(request, 'db.html', context)

def contact(request):
    c = Contact.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
        else:
            form = ContactForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm

    return render(request, 'contact.html', context={'contacts': c, 'form': form})

def index(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm
    return render(request, 'index.html', context={'users':users, 'form': form})