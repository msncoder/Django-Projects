from django.contrib import admin
from .models import SkillsModel
# Register your models here.

@admin.register(SkillsModel)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['title','value','color']
