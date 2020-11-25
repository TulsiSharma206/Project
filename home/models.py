from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Home(models.Model):
    username = models.CharField(max_length=100, blank=False )
    password = models.CharField( max_length=100, blank=False )
    SEX_CHOICES = [('M','Male'), ('F','Female')]
    Phone_number = PhoneNumberField(blank=True)
    Email = models.CharField( max_length=100, blank=True )
    Designation = models.CharField( max_length=100, blank=True)
    sex = models.CharField( max_length=1,choices= SEX_CHOICES, blank=True )
