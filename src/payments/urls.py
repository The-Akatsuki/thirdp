from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^addpayment$', views.addPayment.as_view(), name='addPayment'),
     url(r'^paymentmethods$', views.paymentMethods.as_view(), name='paymentmethods'),
   ]
