# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from . import forms
from . import models
from django.contrib import messages
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
		user = self.request.user
		paymentForm = forms.paymentForm(request.POST)
		payment = paymentForm.save(commit=False)
		payment.user = user
		payment.save()
		messages.success(request, "Payments has been saved!")
		return redirect("payments:paymentmethods")


class paymentMethods(LoginRequiredMixin, generic.TemplateView):
	template_name = "payments/listCreditCard.html"
	http_method_names = ['get', 'post']

	def get(self, request, *args, **kwargs):
		user = self.request.user
		b = models.paymentsDetails.objects.filter(user=user)
		print b
		kwargs["payments"] = b
		return super(paymentMethods, self).get(request, *args, **kwargs)

