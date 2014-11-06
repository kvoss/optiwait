from django.db import models
from clinic.tweets import get_update, TweetError

import logging

logger = logging.getLogger(__name__)

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=1000, blank=True)

    last_update = models.DateTimeField(blank=True)
    est_wait_min = models.IntegerField(blank=True)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # adding additional many-to-many realationship with working hours

    def refresh(self):
        try:
            t, mins = get_update(self.twitter)
            logger.info(' '.join([self.name, str(self.last_update), str(t)]))

            if t > self.last_update:
                self.last_update = t
                self.est_wait_min = mins
                self.save()
        except TweetError:
            pass

    #def get_allvalid(self):
    #    clinics = Clinic.objects.filter(valid=True)
    #    return clinics


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000, blank=True)

    clinic = models.ForeignKey(Clinic)

    def __str__(self):
        return self.name

