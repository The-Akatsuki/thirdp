# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class addPayment(LoginRequiredMixin, generic.TemplateView):
	template_name = "payments/addCreditCard.html"
	http_method_names = ['get', 'post']


class paymentMethods(LoginRequiredMixin, generic.TemplateView):
	template_name = "payments/listCreditCard.html"
	http_method_names = ['get', 'post']