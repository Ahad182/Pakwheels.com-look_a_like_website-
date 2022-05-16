# Generated by Django 3.0.7 on 2022-01-18 11:00

import ckeditor.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteam',
            name='Dores',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=200),
        ),
        migrations.AlterField(
            model_name='carteam',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='carteam',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('powerstairing', 'powerstairing'), ('powerwindow', 'powerwindow'), ('powelockes', 'powerlokes'), ('powermirror', 'powermirror')], max_length=48),
        ),
    ]
