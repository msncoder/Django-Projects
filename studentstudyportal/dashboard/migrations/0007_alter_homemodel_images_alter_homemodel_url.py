# Generated by Django 4.0.5 on 2023-01-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_homemodel_delete_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemodel',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='url',
            field=models.URLField(),
        ),
    ]
