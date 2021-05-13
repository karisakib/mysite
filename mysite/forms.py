# from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Contact

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input is-primary',
                'placeholder': 'Name',
            }),
            'email': forms.TextInput(attrs={
                'class': 'input is-primary',
                'placeholder': 'Email',
            }),
            'message': forms.Textarea(attrs={
                'class': 'textarea is-primary has-fixed-size',
                'placeholder': 'Shoot me a message!',
            }),
        }