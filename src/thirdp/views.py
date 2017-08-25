from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from profiles import models
from ride.models import ridebooking
from django.core.mail import send_mail
from django.http import JsonResponse



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

		bookedRidesData = ridebooking.objects.filter(user=self.request.user)
		print bookedRidesData.__dict__
		if bookedRidesData is not None:
			kwargs['bookedRidesData'] = bookedRidesData
		return super(dashboard, self).get(request, *args, **kwargs)
		

class bookedRides(LoginRequiredMixin, generic.TemplateView):    
	template_name = "ajax_pages/booked_rides.html"

class sendInvitationEmail():
    def get(self, request, *args, **kwargs):
        try:
            send_mail(
                'Subject here',
                'Here is the message.',
                'dineshkaushik829269@gmail.com',
                ['dinesh829269@gmail.com'],
                fail_silently=False,
            )
            data = {'success':True}
        except:
            data = {'success':False}
        return JsonResponse(data)
	

