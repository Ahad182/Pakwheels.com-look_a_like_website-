# Generated by Django 3.0.7 on 2022-01-28 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 19, 11, 7, 533902)),
        ),
    ]
