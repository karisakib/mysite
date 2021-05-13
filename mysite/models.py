from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True

class Contact(models.Model):
    name = models.CharField(max_length=50, unique=False)
    email = models.EmailField(max_length=50, unique=False)
    message = models.TextField()
    # date_created = models.DateTimeField(auto_now_add=True)

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

