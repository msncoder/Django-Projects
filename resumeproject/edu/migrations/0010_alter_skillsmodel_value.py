# Generated by Django 4.0.5 on 2023-01-11 18:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0009_alter_skillsmodel_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsmodel',
            name='value',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
