from datetime import datetime
from email import message
from django.db import models

# Create your models here.
class contacts(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    car_id=models.IntegerField()
    customer_need=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    car_title=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    user_id=models.IntegerField()
    create_date=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.email
