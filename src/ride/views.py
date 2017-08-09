# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
#from . import forms
from . import models

# Create your views here.
class BookRide(LoginRequiredMixin, generic.TemplateView):
	template_name = "ride/book_ride.html"
	http_method_names = ['get', 'post']
	
	def get(self, request, *args, **kwargs):
		return super(BookRide, self).get(request, *args, **kwargs)
