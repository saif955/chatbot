
from django.db import models

     
class UserInput(models.Model):
    input = models.TextField()
    output = models.TextField()

