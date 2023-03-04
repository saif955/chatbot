from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


def homepage(request):
    return render(request, 'temp1.html')
