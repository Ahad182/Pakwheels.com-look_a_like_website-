
from django.db import models


# Create your models here.
class Team(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    Designation=models.CharField(max_length=255)
    img=models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook=models.URLField(max_length=255)
    google=models.URLField(max_length=255)
    twitter=models.URLField(max_length=255)
    email=models.EmailField(max_length=100,default="")
    date=models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return self.f_name