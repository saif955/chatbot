
from django.db import models
from django.forms import ModelForm
     
class UserInput(models.Model):
    input = models.CharField(max_length=5000)