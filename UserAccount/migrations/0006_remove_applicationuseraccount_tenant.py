# Generated by Django 5.1.1 on 2024-11-20 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0005_applicationuseraccount_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationuseraccount',
            name='tenant',
        ),
    ]
