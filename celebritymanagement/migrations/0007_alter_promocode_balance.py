# Generated by Django 5.1.4 on 2024-12-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebritymanagement', '0006_activitylog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='balance',
            field=models.IntegerField(default=199),
        ),
    ]
