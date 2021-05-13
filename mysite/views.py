from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import UserForm, ContactForm
from .models import Contact

def index(request):
    return render(request, 'index.html')

def skills(request):
    skills_list = ['Python', 'NumPy', 'Pandas', 'SciPy', 'Matplotlib', 'Seaborn', 
    'Data Visualization', 'Data Cleaning', 'Data Manipulation', 'Probability Statistics',
    'RStudio', 'SQL', 'HTML-CSS-JavaScript', 'React', 'Java']
    context = {
        'skills_list' : skills_list
    }
    return render(request, 'skills.html', context)

def experience(request):
    return render(request, 'experience.html')

def hobbies(request):
    return render(request, 'hobbies.html')

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
            messages.success(request, "Thank you for your submission!")
            return redirect('contact')
        else:
            form = ContactForm()
            messages.success(error, "Error, please resubmit.")
            return redirect('contact')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm

    return render(request, 'contact.html', context={'contacts': c, 'form': form})

# def index(request):
#     users = User.objects.all()
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserForm
#     return render(request, 'index.html', context={'users':users, 'form': form})