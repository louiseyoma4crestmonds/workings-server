# Generated by Django 5.1.4 on 2024-12-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0008_applicationuseraccount_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='logo',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(default='Name of Tenant', max_length=255),
        ),
    ]
