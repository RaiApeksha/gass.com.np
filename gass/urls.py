from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from contact.views import contact_view
from services.views import services_view
from homepage.views import (
    home_view,
    who_we_are,
    our_history,
    our_strength,
    vision_mission,
    telecommunication,
    power_energy,
    other_services,
)

def about(request):
    return render(request, 'about.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main pages
    path('', home_view, name='home'),
    path('about/', about, name='about'),
    path('services/', services_view, name='services'),
    path('contact/', contact_view, name='contact'),

    # About subpages
    path('about/who-we-are/', who_we_are, name='who-we-are'),
    path('about/our-history/', our_history, name='our-history'),
    path('about/our-strength/', our_strength, name='our-strength'),
    path('about/vision-mission/', vision_mission, name='vision-mission'),

    # Services subpages
    path('services/telecommunication/', telecommunication, name='telecommunication'),
    path('services/power-energy/', power_energy, name='power-energy'),
    path('services/other-services/', other_services, name='other-services'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
