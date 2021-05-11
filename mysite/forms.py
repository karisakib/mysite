from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Contact

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'