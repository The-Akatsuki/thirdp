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


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class dashboard(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.profile.mobile == '':
            request.session['__init_dashboard'] = True
            return redirect("profiles:edit_self")
        b = models.companyDetails.objects.filter(user=self.request.user).count()
        if b==0:
            return redirect("profiles:companyprofile")

        bookedRidesData = ridebooking.objects.filter(user=self.request.user)
        print bookedRidesData.__dict__
        paymentsDetailsData = paymentsDetails.objects.filter(userid=self.request.user)
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


