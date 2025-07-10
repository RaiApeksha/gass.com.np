from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

# About subpages
def who_we_are(request):
    return render(request, 'about/who_we_are.html')

def our_history(request):
    return render(request, 'about/our_history.html')

def our_strength(request):
    return render(request, 'about/our_strength.html')

def vision_mission(request):
    return render(request, 'about/vision_mission.html')

# Services subpages
def telecommunication(request):
    return render(request, 'services/telecommunication.html')

def power_energy(request):
    return render(request, 'services/power_energy.html')

def other_services(request):
    return render(request, 'services/other_services.html')
