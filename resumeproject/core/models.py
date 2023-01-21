from django.db import models
from tinymce import models as tinymce_models
# Create your models here.
class HomeModel(models.Model):
    heading = models.CharField(max_length=50)
    paragraph = tinymce_models.HTMLField()
    

class FormModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=10000)
    