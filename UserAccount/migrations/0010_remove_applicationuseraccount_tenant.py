# Generated by Django 5.1.4 on 2024-12-12 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccount', '0009_alter_tenant_logo_alter_tenant_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationuseraccount',
            name='tenant',
        ),
    ]
