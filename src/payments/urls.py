from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^addpayment$', views.addPayment.as_view(), name='addpayment'),
     url(r'^addpaymentjson$', views.addPaymentJSON.as_view(), name='addpaymentjson'),
     url(r'^paymentmethods$', views.paymentMethods.as_view(), name='paymentmethods'),
   ]
