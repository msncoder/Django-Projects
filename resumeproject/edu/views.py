from django.shortcuts import render
from .models import *
def Skills(request):
    skills = SkillsModel.objects.all()
    context = {'skills':'active','skills':skills}
    return render(request, 'edu/skills.html', context)
