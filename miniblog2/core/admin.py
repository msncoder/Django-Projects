from django.contrib import admin
from .models import Core_Home, Core_About, Contact_Form
# Register your models here.

@admin.register(Core_Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']


@admin.register(Core_About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','desc']

@admin.register(Contact_Form)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','message','number']