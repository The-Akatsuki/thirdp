# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
#from . import forms
from django.contrib import messages
from . import models
import datetime
import requests

# Create your views here.
class BookRide(LoginRequiredMixin, generic.TemplateView):
	template_name = "ride/book_ride.html"
	http_method_names = ['get', 'post']

	def post(self, request):
		user = self.request.user
		postData =  request.POST
		d = datetime.datetime.strptime(postData['Ridedate'], '%d %B %Y %I:%M %p')
		newDateTime = d.strftime('%Y-%m-%d %H:%M:%S')		
		booking_datetime = datetime.datetime.now()
		booking_datetime= booking_datetime.strftime('%Y-%m-%d %H:%M:%S')
		url = "http://lymosrv.ddns.net:7890/lymousine/api/v1/forcorporateapplicationridebooking"
		# print postData['from_country']
		# print postData['from_state']
		# print postData['from_city']
		# print postData["country_id"]
		# print postData["state_id"]
		# print postData["city_id"]
		# print postData["distance"]
		# print postData["cost"]
		# print postData["duration"]
		payload = {
					"pickup_lat":postData['from_lat'], 
					"pickup_long":postData['from_lon'],	
					"drop_lat":postData['to_lat'], 
					"drop_long":postData['to_lon'],
					"pickup_address":postData['from'], 
					"drop_address":postData['to'], 
					"ride_datetime":newDateTime, 
					"noof_passengers":1, 
					"vehicle_type":postData['type'],
					"ride_booked_by":1, 
					"passenger":postData['passengerid'],
					"booking_DateTime":booking_datetime,
					"est_time": postData["duration"],
					"est_cost": postData["cost"],
					"est_dist_bw_location": postData["distance"],
					"ride_booked_by":1,
					"ride_type":1,
					"country":postData['country_id'],
					"state":postData['state_id'],
					"city":postData['city_id']
				 }


		# print payload

		response = requests.post(url, json = payload)
		# print "response text"
		# print response.text
		p = models.ridebooking( pickup_lat=postData['from_lat'], 
								pickup_long=postData['from_lon'],	
								drop_lat=postData['to_lat'], 
								drop_long=postData['to_lon'],
								pickup_address=postData['from'], 
								drop_address=postData['to'], 
								ride_datetime=newDateTime, 
								noof_passengers=1, 
								vehicle_type=postData['type'],
								ride_booked_by=1, 
								passenger=postData['passengerid'],
								passenger_email=postData['email'],
								status='New Ride Booked',
								user = user)	
		p.save()	
		messages.success(request, "Your Ride has been booked!")
		return redirect("dashboard")			
	
	def get(self, request, *args, **kwargs):
		user = self.request.user
		b = models.ridebooking.objects.filter(user=user)
		print b.__dict__
		return super(BookRide, self).get(request, *args, **kwargs)
