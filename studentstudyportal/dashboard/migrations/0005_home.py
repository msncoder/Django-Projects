# Generated by Django 4.0.5 on 2023-01-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]