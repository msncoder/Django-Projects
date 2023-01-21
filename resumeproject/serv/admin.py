from django.contrib import admin
from .models import ServModel

# Register your models here.
@admin.register(ServModel)
class ServAdmin(admin.ModelAdmin):
    list_display = ['icon','title','desc']
