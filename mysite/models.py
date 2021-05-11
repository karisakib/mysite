from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True

class Contact(models.Model):
    email = models.EmailField(max_length=50, unique=False)
    message = models.TextField()

# class ExampleModel(models.Model):
#     # character field, has max_length
#     name = models.CharField(max_length=50, unique=False)

#     # email field
#     email = models.EmailField(max_length=50, unique=True)

#     # text field used for large fields of text
#     notes = models.TextField()

#     # auto_now=True means it updates date when model is saved
#     date_saved = models.DateTimeField(auto_now=True) 

#     # auto_now_add=True means it sets date when model created
#     date_created = models.DateTimeField(auto_now_add=True)

#     # saves files to MEDIA_ROOT/uploads/ folder
#     # MEDIA_ROOT is defined in `settings.py`
#     # file = models.FileField(upload_to='uploads/')

#     # stores IP address
#     # IP address can be gotten from the request object in the view
#     # either request.META.get("REMOTE_ADDR") or request.META.get('HTTP_X_FORWARDED_FOR')
#     ip_address = models.GenericIPAddressField()

# class Car(models.Model):
#     make = models.CharField(max_length=50)
#     trim = models.CharField(max_length=50)
#     color = models.CharField(max_length=50)

# one to one relationship
# each Car has one Stats
# each Stats has one Car
# class Stats(models.Model):
#     horsepower = models.CharField(max_length=50)
#     torque = models.EmailField(max_length=50)
#     car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True)
