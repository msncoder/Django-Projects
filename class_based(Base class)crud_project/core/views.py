from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserRegistration
from django.views.generic.base import TemplateView, RedirectView, View
# Create your views here.

class Add_Show_View(TemplateView):
    template_name = 'core/addandshow.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UserRegistration()
        user = User.objects.all()
        context = {'form':form, 'user':user}
        return context


    def post(self, request):
        form = UserRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            reg = User(name=nm,email=em,password=pwd)
            reg.save()
        return HttpResponseRedirect('/')


class UserUpdateView(View):
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        form = UserRegistration(instance = pi)
        return render(request, 'core/update.html',{'form':form})
    
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        form = UserRegistration(request.POST, instance=pi)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pwd = form.cleaned_data['password']
            reg = User(name=nm,email=em,password=pwd)
            reg.save()
        return HttpResponseRedirect('/')



class UserDeleteView(RedirectView):
    url = ('/')
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

