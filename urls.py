from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import (
    services_view,
    ict_services,
    telecommunication,
    power_energy,
    other_services,
)

# Define simple views for home, about, and contact pages
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services_view, name='services'),  # Use imported view
    path('contact/', contact, name='contact'),

    # Service subpages
    path('services/ict-services/', ict_services, name='ict-services'),
    path('services/telecommunication/', telecommunication, name='telecommunication'),
    path('services/power-energy/', power_energy, name='power-energy'),
    path('services/other-services/', other_services, name='other-services'),
]
