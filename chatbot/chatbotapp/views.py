from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest

from chatbotapp.forms import UserInputForm
from .models import UserInput
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random


def homepage(request):
    form = UserInputForm(request.POST)
    form.save()
    print(request.POST)
    return render(request, 'temp1.html', {'form': form})
