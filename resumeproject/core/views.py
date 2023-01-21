from django.shortcuts import render, HttpResponseRedirect
from .models import HomeModel, FormModel
from .forms import ResponseForm
def Home(request):
    homemodel = HomeModel.objects.all()
    context = {'home':'active','homemodels':homemodel}
    return render(request,"core/home.html", context)

def Contact(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            sb = form.cleaned_data['subject']
            me = form.cleaned_data['message']
            reg = FormModel(name=nm,email=em,subject=sb,message=me)
            reg.save()
            return HttpResponseRedirect('/contact/')
    else:
        form = ResponseForm()

    context = {'contact':'active','form':form}
    return render(request,"core/contact.html", context)
