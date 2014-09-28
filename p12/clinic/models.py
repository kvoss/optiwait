from django.db import models

# Create your models here.

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=1000, blank=True)

    # adding additional many-to-many realationship with working hours
    # for now logic assumer 9-5


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000, blank=True)

    clinic = models.ForeignKey(Clinic)


