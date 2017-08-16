# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class paymentsDetails(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    nameOnCard = models.CharField(max_length=250, null=True)
    cardNumber = models.CharField(max_length=20,null=True)
    expirationDateMM = models.IntegerField()
    expirationDateYY = models.IntegerField()
    cvcCode = models.IntegerField()
    address = models.TextField(null=True)
    city = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    zipCode = models.CharField(max_length=250, blank=True)



