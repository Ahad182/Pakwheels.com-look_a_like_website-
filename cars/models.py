
from datetime import datetime
from django.db import models
from django.forms import BooleanField
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.
class CarTeam(models.Model):

    feature_choice=(
        ('powerstairing','powerstairing'),
        ('powerwindow','powerwindow'),
        ('powelockes','powerlokes'),
        ('powermirror','powermirror'),
    )
    state_choice=(
        ('pu','punjab'),
        ('bl','blochistan'),
        ('kpk','khaibar'),
        ('snd','sind'),
    )
    dore_choice=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    year_choice=[]
    for r in range(2000,datetime.now().year+1):
        year_choice.append((r,r))

    car_name=models.CharField(max_length=255)
    description=RichTextField()
    car_color=models.CharField(max_length=30)
    city=models.CharField(max_length=255)
    model=models.CharField(max_length=255)
    year=models.IntegerField(choices=year_choice)
    state=models.CharField(choices=state_choice,max_length=30)
    condition=models.CharField(max_length=255)
    features=MultiSelectField(choices=feature_choice)
    car_photo=models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo1=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo2=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo3=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo4=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    price=models.IntegerField()
    bode_style=models.CharField(max_length=30)
    engine=models.CharField(max_length=30)
    transmision=models.CharField(max_length=30)
    interior=models.CharField(max_length=30)
    passengers=models.CharField(max_length=30)
    miles=models.IntegerField()
    Dores=models.CharField(choices=dore_choice , max_length=200)
    is_featured=models.BooleanField(default=False)
    fuel_type=models.CharField(max_length=30)
    Number_owner=models.CharField(max_length=30)
    date_created=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) :
        return self.car_name

