# Generated by Django 4.0.5 on 2023-01-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_alter_skillsmodel_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsmodel',
            name='value',
            field=models.IntegerField(),
        ),
    ]
