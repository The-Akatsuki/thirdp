from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    mobile = models.CharField(max_length=20,null=True,verbose_name="Mobile")
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)

userType_CHOICES = {
        ("company_secretary", "company Secretary"),
        ("third_party_desk", "Third party travel desk Secretary")
    }

class companyDetails(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    companyName = models.CharField(max_length=250, null=True,verbose_name="Company Name")
    phone = models.CharField(max_length=20,null=True,verbose_name="phone")
    address = models.TextField(null=True, verbose_name="address")
    city = models.CharField(max_length=250, blank=True,verbose_name="city")
    state = models.CharField(max_length=250, blank=True,verbose_name="state")
    zipCode = models.CharField(max_length=250, blank=True,verbose_name="zip Code")
    country = models.CharField(max_length=250, blank=True,verbose_name="country")
    userType = models.CharField(max_length=50, choices=userType_CHOICES, verbose_name="user Type", default='company_secretary')
    

