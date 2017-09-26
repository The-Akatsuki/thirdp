# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from . import forms
from . import models
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import companyDetails
import requests
import json
from django.http import JsonResponse

# Create your views here.
import environ
env = environ.Env()
LYMOSRV_URL = env('LYMOSRV_URL')

class addPayment(LoginRequiredMixin, generic.TemplateView):
    template_name = "payments/addPaymentMethod.html"
    http_method_names = ['get', 'post']

    def get(self, request, id=None, *args, **kwargs):
        if "paymentForm" not in kwargs:
            if id is not None:
                paymentData = models.paymentsDetails.objects.filter(id=id).first()
                kwargs["paymentForm"] = forms.paymentForm(instance=paymentData)
            else:
                kwargs["paymentForm"] = forms.paymentForm()
        return super(addPayment, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            user = self.request.user
            paymentData = models.paymentsDetails.objects.filter(card_number=request.POST['cardNumber']).first()
            paymentForm = forms.paymentForm(request.POST, instance=paymentData)
            payment = paymentForm.save(commit=False)
            payment.userid = user
            payment.save()
            messages.success(request, "Payments has been saved!")
            data = companyDetails.objects.filter(user=request.user.id).first()
            #hiting the api for save
            url = LYMOSRV_URL+"lymousine/api/v1/thirdpartycarddetailssave"
            payload = {
                "company":str(data.lymo_company_id),
                "card_name": request.POST['nameOnCard'],
                "card_number": request.POST['cardNumber'],
                "exp_date_mm": request.POST['expirationDateMM'],
                "exp_date_yy": request.POST['expirationDateYY'],
                "card_short_name": 1,
                "cvv_code": request.POST['cvcCode'],
                "address": request.POST['address'],
                "city": request.POST['city'],
                "state": request.POST['state'],
                "zip_code":request.POST["zipCode"],
                "created_by":str(data.lymo_profile_id),
                "updated_by":str(data.lymo_profile_id)
                }
            print payload
            print url
            response = requests.post(url, json = payload)
            data_to_store =json.loads(response.text)
            print data_to_store
            if data_to_store["success"]== True:
                lymo_company_id = data_to_store["data"]["company"]              
                print request.user.id
                data = models.paymentsDetails.objects.filter(userid=request.user.id).update(lymo_company_id=lymo_company_id)
            print response.text

            if '__init_dashboard_payments' in request.session:
                messages.success(request, "Payment Method has been saved!")
                del request.session['__init_dashboard_payments']
                return redirect("dashboard")

            if '__add_payment_revert' in request.session:
                del request.session['__add_payment_revert']
                messages.success(request, "Payment Method has been saved!")
                return redirect("dashboard")
            
        except Exception as e:
            print e 
        return redirect("payments:paymentmethods")


class editPayment(LoginRequiredMixin, generic.TemplateView):
    template_name = "payments/editPaymentMethod.html"
    http_method_names = ['get', 'post']

    def get(self, request, id=None, *args, **kwargs):
        if "paymentForm" not in kwargs:
            if id is not None:
                paymentData = models.paymentsDetails.objects.filter(id=id).first()
                kwargs["paymentForm"] = forms.paymentForm(instance=paymentData)
            else:
                kwargs["paymentForm"] = forms.paymentForm()
        return super(editPayment, self).get(request, *args, **kwargs)

    def post(self, request, id=None, *args, **kwargs):
        try:
            user = self.request.user
            paymentData = models.paymentsDetails.objects.filter(id=id).first()
            #print "Line 103, id:",id
            #print paymentData
            paymentForm = forms.paymentForm(request.POST, instance=paymentData)
            payment = paymentForm.save()
            messages.success(request, "Payments has been saved!")
            data = companyDetails.objects.filter(user=request.user.id).first()
            #hiting the api for save
            url = LYMOSRV_URL+"lymousine/api/v1/thirdpartycarddetailssave"
            payload = {
                "company":str(data.lymo_company_id),
                "card_name": request.POST['nameOnCard'],
                "card_number": request.POST['cardNumber'],
                "exp_date_mm": request.POST['expirationDateMM'],
                "exp_date_yy": request.POST['expirationDateYY'],
                "card_short_name": 1,
                "cvv_code": request.POST['cvcCode'],
                "address": request.POST['address'],
                "city": request.POST['city'],
                "state": request.POST['state'],
                "zip_code":request.POST["zipCode"],
                "created_by":str(data.lymo_profile_id),
                "updated_by":str(data.lymo_profile_id)
                }
            #print payload
            #print url
            response = requests.post(url, json = payload)
            data_to_store =json.loads(response.text)
            print data_to_store
            if data_to_store["success"]== True:
                lymo_company_id = data_to_store["data"]["company"]              
                print request.user.id
                data = models.paymentsDetails.objects.filter(userid=request.user.id).update(lymo_company_id=lymo_company_id)
            print response.text

            if '__init_dashboard_payments' in request.session:
                messages.success(request, "Payment Method has been saved!")
                del request.session['__init_dashboard_payments']
                return redirect("dashboard")

            if '__add_payment_revert' in request.session:
                del request.session['__add_payment_revert']
                messages.success(request, "Payment Method has been saved!")
                return redirect("dashboard")
            
        except Exception as e:
            print e 
        return redirect("payments:paymentmethods")


class addPaymentJSON(LoginRequiredMixin, generic.TemplateView):
    template_name = "payments/addPaymentMethod.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        if "paymentForm" not in kwargs:
            kwargs["paymentForm"] = forms.paymentForm()
        return super(addPayment, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            user = self.request.user
            paymentForm = forms.paymentForm(request.POST)
            payment = paymentForm.save(commit=False)
            payment.userid = user
            payment.save()
            messages.success(request, "Payments has been saved!")
            data = companyDetails.objects.filter(user=request.user.id).first()
            #hiting the api for save
            url = LYMOSRV_URL+"lymousine/api/v1/thirdpartycarddetailssave"
            payload = {
                "company":str(data.lymo_company_id),
                "card_name": request.POST['nameOnCard'],
                "card_number": request.POST['cardNumber'],
                "exp_date_mm": request.POST['expirationDateMM'],
                "exp_date_yy": request.POST['expirationDateYY'],
                "card_short_name": 1,
                "cvv_code": request.POST['cvcCode'],
                "address": request.POST['address'],
                "city": request.POST['city'],
                "state": request.POST['state'],
                "zip_code":request.POST["zipCode"],
                "created_by":str(data.lymo_profile_id),
                "updated_by":str(data.lymo_profile_id)
                }
            print payload
            print url
            response = requests.post(url, json = payload)
            data_to_store =json.loads(response.text)
            print data_to_store
            if data_to_store["success"]== True:
                lymo_company_id = data_to_store["data"]["company"]              
                print request.user.id
                data = models.paymentsDetails.objects.filter(userid=request.user.id).update(lymo_company_id=lymo_company_id)
            print response.text
        except Exception as e:
            print e 
        return JsonResponse(response)

class addPaymentrevert(LoginRequiredMixin, generic.TemplateView):
    template_name = "payments/addPaymentMethod.html"
    http_method_names = ['get', 'post']

    def post(self, request, *args, **kwargs):
        request.session['__add_payment_revert'] = True
        request.session['__book_ride_form_data'] = request.POST
        if "paymentForm" not in kwargs:
            kwargs["paymentForm"] = forms.paymentForm()
        return super(addPaymentrevert, self).get(request, *args, **kwargs)

        


class deletePayment(LoginRequiredMixin, generic.TemplateView):
    template_name = "payments/addPaymentMethod.html"
    http_method_names = ['get', 'post']

    def get(self, request, id=None, *args, **kwargs):
        if "paymentForm" not in kwargs:
            paymentData = models.paymentsDetails.objects.filter(id=id).delete()
            return redirect("payments:paymentmethods")
        return super(addPayment, self).get(request, *args, **kwargs)


class paymentMethods(LoginRequiredMixin, generic.TemplateView):
    template_name = "payments/listCreditCard.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        b = models.paymentsDetails.objects.filter(userid=user)
        print b
        if b is not None:
            for item in b:
                item['cardNumber'] = b[:2] + '*******' + b[3:]
        kwargs["payments"] = b
        return super(paymentMethods, self).get(request, *args, **kwargs)

