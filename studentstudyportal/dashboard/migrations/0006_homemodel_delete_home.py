# Generated by Django 4.0.5 on 2023-01-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
