
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbotapp.urls')),
    path('accounts/', include('allauth.urls')),

    
]

