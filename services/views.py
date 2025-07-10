from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project, Service

def telecommunication(request):
    telecom_services = Service.objects.filter(category='Telecom')
    return render(request, 'services/telecommunication.html', {'telecom_services': telecom_services})

def power_energy(request):
    power_services = Service.objects.filter(category='Power')
    return render(request, 'services/power_energy.html', {'power_services': power_services})

def ict_services(request):
    ict_services = Service.objects.filter(category='ICT')
    return render(request, 'services/ict_services.html', {'ict_services': ict_services})

def other_services(request):
    other_services = Service.objects.filter(category='Support')
    return render(request, 'services/other_services.html', {'other_services': other_services})

def services_view(request):
    categories = ['All', 'Telecom', 'ICT', 'Power', 'Support']
    selected_category = request.GET.get('category', 'All')

    if selected_category != 'All':
        projects = Project.objects.filter(category=selected_category)
    else:
        projects = Project.objects.all()

    paginator = Paginator(projects, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'services': Service.objects.all(),
        'projects': page_obj,
        'selected_category': selected_category,
        'categories': categories,
    }
    return render(request, 'services.html', context)
