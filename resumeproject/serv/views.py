from django.shortcuts import render
from .models import ServModel

def Services(request):
    servicesdata = ServModel.objects.all()
    context = {'services':'active','servicesdata':servicesdata}
    return render(request,'serv/services.html', context)
