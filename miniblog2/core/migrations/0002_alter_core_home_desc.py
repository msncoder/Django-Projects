# Generated by Django 4.0.5 on 2022-10-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core_home',
            name='desc',
            field=models.TextField(),
        ),
    ]
