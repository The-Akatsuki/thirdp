# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class paymentsDetails(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL)
    nameOnCard = models.CharField(max_length=250, null=True,verbose_name="Name On Card")
    cardNumber = models.CharField(max_length=20,null=True,verbose_name="Card Number")
    expirationDateMM = models.IntegerField(verbose_name="expiration Date (MM)")
    expirationDateYY = models.IntegerField(verbose_name="expiration Date (YY)")
    cvcCode = models.IntegerField(verbose_name="CVV Code")
    address = models.TextField(null=True,verbose_name="Address")
    city = models.CharField(max_length=250, blank=True,verbose_name="City")
    state = models.CharField(max_length=250, blank=True,verbose_name="State")
    zipCode = models.CharField(max_length=250, blank=True,verbose_name="Zip Code")
    cardshortname = models.CharField(max_length=25,null=True,verbose_name="Card short Name")
