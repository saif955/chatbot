from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='signin'),
    path('chat/', views.chat_homepage, name='upload'),
    path('post/', views.post, name='post'),
    path('chat/logout', views.logout_view, name='logout')
  
]