from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from profiles import models


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class dashboard(LoginRequiredMixin, generic.TemplateView):	
	template_name = "dashboard.html"

	def get(self, request, *args, **kwargs):
		print self.request.user
		b = models.companyDetails.objects.filter(user=self.request.user).count()
		if b ==0:
			 return redirect("profiles:companyprofile")
		return super(dashboard, self).get(request, *args, **kwargs)
		

class bookedRides(LoginRequiredMixin, generic.TemplateView):	
	template_name = "ajax_pages/booked_rides.html"

