# Generated by Django 4.0.5 on 2023-01-09 14:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemodel',
            name='paragraph',
            field=tinymce.models.HTMLField(max_length=2000),
        ),
    ]