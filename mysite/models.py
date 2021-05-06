from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    trim = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

# one to one relationship
# each Car has one Stats
# each Stats has one Car
class Stats(models.Model):
    horsepower = models.CharField(max_length=50)
    torque = models.EmailField(max_length=50)
    car = models.OneToOneField(Car, on_delete=models.CASCADE, primary_key=True)


# I'm getting this error and I've tried looking into the docs and notebooks, still can't figure out where I went wrong.

# stat = Stats.objects.create(car=c.id, horsepower="400", torque="380")

# I get this error below

# if value is not None and not isinstance(value, self.field.remote_field.model._meta.concrete_model):
# --> 215             raise ValueError(
#     216                 'Cannot assign "%r": "%s.%s" must be a "%s" instance.' % (
#     217                     value,

# SOLUTION: PASS INSTANCE VARIABLE