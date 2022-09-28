from django.contrib import admin

# Register your models here.
from .models import Person #import the Person model

# Register your models here.
admin.site.register(Person)