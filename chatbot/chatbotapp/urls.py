from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.homepage),
    path('doctor/', views.doctor),
    path('', views.drink_list)

]