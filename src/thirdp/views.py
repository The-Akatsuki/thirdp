from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from profiles import models
from ride.models import ridebooking
from payments.models import paymentsDetails
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import requests

import environ
env = environ.Env()
LYMOSRV_URL = env('LYMOSRV_URL')
LYMO_RIDE_ESTIMATE_URL = env('LYMO_RIDE_ESTIMATE_URL')


class HomePage(generic.TemplateView):
    template_name = "home.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class dashboard(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.profile.mobile == '' or user.profile.mobile == None:
            request.session['__init_dashboard_profile'] = True
            return redirect("profiles:edit_self")
        companyDetailsData = models.companyDetails.objects.filter(user=self.request.user).count()
        if companyDetailsData==0:
            request.session['__init_dashboard_company'] = True
            return redirect("profiles:companyprofile")
        paymentsDetailsData = paymentsDetails.objects.filter(userid=self.request.user)
        if paymentsDetailsData.count() ==0:
            request.session['__init_dashboard_payments'] = True
            return redirect("payments:addpayment")        

        url = LYMOSRV_URL+"lymousine/api/v1/thirdpartycompanyinfo"
        payload = {
            "email_id": user.email
        }
        print payload
        companyStatus = requests.post(url, json = payload);
        companyStatusText = companyStatus.__dict__
        kwargs['companyStatus'] = False
        if 'success' in companyStatusText:
            if companyStatusText.success == False:
                print "line 52"
                kwargs['companyStatus'] = False
            else:
                print "line 55"
                kwargs['companyStatus'] = True 

        print kwargs['companyStatus']

        kwargs['lymoSrvURL'] = LYMOSRV_URL
        kwargs['lymoRideEstimateURL'] = LYMO_RIDE_ESTIMATE_URL

        bookedRidesData = ridebooking.objects.filter(user=self.request.user)
        print bookedRidesData.__dict__
        if bookedRidesData is not None:
            kwargs['bookedRidesData'] = bookedRidesData
            kwargs['paymentsDetailsData'] = paymentsDetailsData            
        return super(dashboard, self).get(request, *args, **kwargs)


class bookedRides(LoginRequiredMixin, generic.TemplateView):
    template_name = "ajax_pages/booked_rides.html"

@csrf_exempt
def sendInvitationEmail(request):
    print request
    try:
        mailResponse = send_mail(
            'Subject here',
            'Here is the message.',
            'lymousinecar@gmail.com',
            ['lymousinecar@gmail.com'],
            fail_silently=False,
        )
        print mailResponse
        data = {'success':True}
    except:
        data = {'success':False}
    return JsonResponse(data)


