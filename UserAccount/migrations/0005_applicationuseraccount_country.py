# Generated by Django 5.1.1 on 2024-10-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0004_applicationuseraccount_is_first_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationuseraccount',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
    ]
