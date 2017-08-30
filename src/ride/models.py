# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class ridebooking(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
	ride_id = models.CharField(max_length=200, null=True)
	pickup_long = models.CharField(max_length=250, null=True)
	pickup_lat = models.CharField(max_length=250, null=True)
	drop_lat = models.CharField(max_length=250, null=True)
	drop_long = models.CharField(max_length=250, null=True)
	pickup_address = models.CharField(max_length=250, null=True)
	drop_address = models.CharField(max_length=250, null=True)
	ride_datetime = models.CharField(max_length=50, null=True)
	passenger = models.CharField(max_length=250, null=True)
	passenger_email = models.CharField(max_length=250, null=True)
	vehicle_type = models.CharField(max_length=250, null=True)
	noof_passengers = models.CharField(max_length=250, null=True)
	ride_booked_by = models.CharField(max_length=250, null=True)
	status = models.CharField(max_length=250, null=True)
