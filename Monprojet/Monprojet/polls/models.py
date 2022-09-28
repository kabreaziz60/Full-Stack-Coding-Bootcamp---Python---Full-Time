from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
#from django.db import models import the models package. This line is already existing as soon as we use 'startapp'

#Must inherit from Django Model class
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    e_mail = models.CharField(max_length=30)
    number_pet = models.IntegerField(
        validators = [
            MaxValueValidator(10),
            MinValueValidator(1)
        ])