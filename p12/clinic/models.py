from django.db import models

# Create your models here.


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100, default='')

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    clinic = models.ForeignKey(Clinic)

