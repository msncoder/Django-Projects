from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class SkillsModel(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
     )
    color = models.CharField(max_length=100, null=True)