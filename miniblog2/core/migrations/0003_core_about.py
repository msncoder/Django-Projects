# Generated by Django 4.0.5 on 2022-10-30 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_core_home_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Core_About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
    ]
