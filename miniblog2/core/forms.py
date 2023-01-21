from cProfile import label
from socket import fromshare
from django import forms
from .models import Contact_Form, Core_Home
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Contact_Form 
        fields = ['name','email','message','address','number']
        labels = {'name':'Name','email':'Email','message':'Message','address':'Address','number':'Phone Number'}
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'message' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'number' : forms.TextInput(attrs={'class':'form-control'}),
        }

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmation Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'username' : 'Name',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email'
        },
        widgets = {
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True ,'class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autofocus':True, 'class':'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Core_Home
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'desc' : forms.Textarea(attrs={'class':'form-control'})
            }
