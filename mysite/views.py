from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from mysite.models import Car, Stats

# view using render()
def index(request):
    name = 'Kari Sakib'
    context = {
        'name' : name
    }
    return render(request, 'index.html', context)

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
