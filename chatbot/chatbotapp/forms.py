from django.forms import ModelForm
from .models import*
from django import forms


class UserInputForm(ModelForm):
     input = forms.TextInput()
     class Meta:
          model = UserInput
          fields = [ "input" ]
