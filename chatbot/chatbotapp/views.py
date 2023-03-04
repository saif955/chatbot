from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import random

def homepage(request):
    return render(request, 'temp1.html', {'number': random.randint(1, 50)})
