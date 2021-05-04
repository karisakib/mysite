from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

# one to one relationship
# each User has one Profile
# each Profile has one User
class Profile(models.Model):
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# one to many relationship
# each User has many Alerts
# each Alert has one User
class Alerts(models.Model):
    message = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# many to many relationship
# each User has many Groups
# each Group has many Users
class Group(models.Model):
    users = models.ManyToManyField(User)