from django.shortcuts import render, HttpResponseRedirect
from .models import Core_Home, Contact_Form, Core_About
from .forms import RegistrationForm, SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.core.cache import cache
# Create your views here.

def Home(request):
    home_posts = Core_Home.objects.all()
    return render(request,'core/home.html',{'home_posts':home_posts})


def About(request):
    about_post = Core_About.objects.all()
    return render(request,'core/about.html',{'about_post':about_post})


def Contact(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            me = form.cleaned_data['message']
            ad = form.cleaned_data['address']
            nu = form.cleaned_data['number']
            reg = Contact_Form(name=nm,email=em,message=me,address=ad,number=nu)
            reg.save()
            form = RegistrationForm()
    else:
        form = RegistrationForm()

    return render(request,'core/contact.html',{'fm':form})

def Dashboard(request):
    if request.user.is_authenticated:
        posts = Core_Home.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip',0)
        ct = cache.get('count', version = user.pk)
        return render(request,'core/dashboard.html',{'posts':posts,'f_name':full_name,'gps':gps, 'ip':ip, 'ct':ct})
    else:
        return HttpResponseRedirect('/login/')

def User_Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def User_Signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Congrats you have become an author')
                user = form.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request,'core/signup.html',{'form':form})


def User_Login(request):
    if not request.user.is_authenticated:
        if request.method  == 'POST':
            form = LoginForm(request=request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'core/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def AddPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Core_Home(title=title,desc=desc)
                messages.success(request, 'Add Post Successfully')
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'core/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def UpdatePost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Core_Home.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                messages.success(request, 'Update Post Successfully')
                form.save()
        else:
            pi = Core_Home.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'core/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def DeletePost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Core_Home.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')