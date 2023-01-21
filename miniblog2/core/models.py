from ctypes import addressof
from email import message
from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Core_Home(models.Model):
    title = models.CharField(max_length=70)
    desc = tinymce_models.HTMLField()

class Core_About(models.Model):
    desc = tinymce_models.HTMLField()

class Contact_Form(models.Model):
    name = models.CharField(max_length = 70)
    email = models.EmailField(max_length = 100)
    message = models.TextField()
    address = models.TextField()
    number = models.CharField(max_length = 11)

