from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    GENDER_CHOICE =(
        ('M','Male'),
        ('F','female'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE)
    mobile_1 = models.CharField(max_length=100)
    mobile_2 = models.CharField(max_length=100)
    mobile_3 = models.CharField(max_length=100)
    address_1 = models.TextField()
    city     =  models.CharField(max_length=100)
    country  = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('tenant_detail',kwargs={'pk':self.pk})
