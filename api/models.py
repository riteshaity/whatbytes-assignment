from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass 


class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField()
    address = models.TextField()

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField()
    address = models.TextField()
    speciality = models.CharField(max_length=300)

class Mapping(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)