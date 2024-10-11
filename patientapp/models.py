from django.db import models

# Create your models here.
class patientregister(models.Model):
    Name=models.CharField(max_length=25)
    Address = models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Contact=models.BigIntegerField()
    Age=models.BigIntegerField(default=0)
    Username= models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='')

class appointment(models.Model):
    Name=models.CharField(max_length=25)
    Email=models.CharField(max_length=25)
    Date=models.DateField()
    Symptoms = models.CharField(max_length=200)
    Contact = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='')


class pay(models.Model):
    BankName=models.CharField(max_length=25)
    Branch=models.CharField(max_length=25)
    cardno=models.CharField(max_length=25)
    cardholder = models.CharField(max_length=200)
    amount = models.IntegerField()