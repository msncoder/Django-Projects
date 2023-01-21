from django.db import models
from tinymce import models as tinymce_models
# Create your models here.
class ServModel(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = tinymce_models.HTMLField()