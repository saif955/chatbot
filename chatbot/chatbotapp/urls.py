from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='upload'),
    path('post/', views.post, name='post')
  
]