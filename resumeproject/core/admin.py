from django.contrib import admin
from . models import HomeModel,FormModel
# Register your models here.

@admin.register(HomeModel)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['heading', 'paragraph']

@admin.register(FormModel)
class FormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message',]