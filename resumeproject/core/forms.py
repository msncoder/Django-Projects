from django import forms
from .models import FormModel

class ResponseForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['name','email','subject','message']
        labels = {'name':'Name','email':'Email','subject':'Subject','message':'Message'}
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'message' : forms.TextInput(attrs={'class':'form-control'}),
        }