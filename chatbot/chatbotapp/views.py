from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from .serializers import DrinkSerializer
from .models import Drink
import random

def homepage(request):
    return render(request, 'temp1.html', {'number': random.randint(1, 50)})

def doctor(request):
    return HttpResponse('doctor is not here')

def drink_list(request):
    drinks= Drink.objects.all()
    serializer= DrinkSerializer(drinks, many= True)
    return JsonResponse(serializer.data, safe=False)
 