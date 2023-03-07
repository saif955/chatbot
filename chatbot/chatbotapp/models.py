
from django.db import models

class Drink(models.Model):
    Name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.Name + ' ' + self.description       