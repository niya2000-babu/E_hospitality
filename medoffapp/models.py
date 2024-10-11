from django.db import models

# Create your models here.

class doctorsregister(models.Model):
    Name = models.CharField(max_length=25)
    Email=models.CharField(max_length=50)
    # Contact = models.BigIntegerField()
    Contact=models.BigIntegerField()
    Address = models.CharField(max_length=50)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.IntegerField()
    country = models.CharField(max_length=20)
    Specialization = models.CharField(max_length=100)
    photo = models.FileField(upload_to="file")
    qual = models.FileField(upload_to="file")
    exp = models.FileField(upload_to="file")
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='')
class shedule(models.Model):
     Name = models.CharField(max_length=25)
     Age = models.CharField(max_length=50,null=True)
     Contact = models.CharField(max_length=50,null=True)
     Email = models.CharField(max_length=50,null=True)
     Gender = models.CharField(max_length=20,null=True)
     Time = models.TimeField(max_length=20,null=True)



class eprescripotion(models.Model):
    Name = models.CharField(max_length=25)
    Age = models.CharField(max_length=50)
    Gender = models.CharField(max_length=20)
    Medicines = models.CharField(max_length=50)
    Test = models.CharField(max_length=20)
    bill = models.IntegerField(null=True)
