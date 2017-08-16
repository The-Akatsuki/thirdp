# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class addPayment(LoginRequiredMixin, generic.TemplateView):
	template_name = "payments/addPaymentMethod.html"
	http_method_names = ['get', 'post']

	def get(self, request, *args, **kwargs):
		if "paymentForm" not in kwargs:
			kwargs["paymentForm"] = forms.paymentForm()
		return super(addPayment, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		paymentForm = forms.paymentForm(request.POST)
		paymentForm.save()
		messages.success(request, "Payments has been saved!")
		return redirect("payments:paymentmethods")


class paymentMethods(LoginRequiredMixin, generic.TemplateView):
	template_name = "payments/listCreditCard.html"
	http_method_names = ['get', 'post']
