from django.contrib import admin
from django.urls import path, include
urlpatterns = [path('admin/', admin.site.urls), path('alerts/', include('alerts.urls')), path('logs/', include('log_processing.urls'))]
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Add a simple view for the root URL
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home),  # This will handle the root URL
    path('admin/', admin.site.urls),
    path('alerts/', include('alerts.urls')),
    path('logs/', include('log_processing.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
