from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserRegistration
# Create your views here.

def Add_Show(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            reg = User(name=nm,email=em,password=pwd)
            reg.save()
    else:
        form = UserRegistration()
    user = User.objects.all()
    return render(request, 'core/addandshow.html',{'form':form, 'user':user})

def Update_Data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = UserRegistration(request.POST, instance=pi)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            reg = User(name=nm,email=em,password=pwd)
            reg.save()
    else:
        pi = User.objects.get(pk=id)
        form = UserRegistration(instance = pi)
    return render(request, 'core/update.html',{'form':form})

def Delete_Data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')