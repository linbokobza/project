from django.db import models

# Create your models here.

class login(models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=20)


class signUp(models.Model):
    name=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    phone=models.IntegerField(max_length=10)
    adress=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=20)
