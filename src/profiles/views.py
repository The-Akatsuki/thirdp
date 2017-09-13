from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
import requests


class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            profile = get_object_or_404(models.Profile, slug=slug)
            user = profile.user
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        return super(ShowProfile, self).get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        if '__init_dashboard' in request.session:
            print "Session Found";
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        if '__init_dashboard' in request.session:
            url = "https://lymosrv.ddns.net/lymousine/api/v1/thirdpartyusersave"
            payload = {
                "name": user.name,
                "email": user.email,
                "mobile_no": request.POST['mobile'],
                "bio": request.POST['bio']
            }
            print payload
            response = requests.post(url, json = payload)
            del request.session['__init_dashboard']
            messages.success(request, "Profile details saved!")
            return redirect("dashboard")
        else:
            url = "https://lymosrv.ddns.net/lymousine/api/v1/thirdpartyuser/"+user.email
            payload = {
                "name": user.name,
                "mobile_no": request.POST['mobile'],
                "bio": request.POST['bio']
            }
            print payload
            response = requests.post(url, json = payload)
            print response

        messages.success(request, "Profile details saved!")
        return redirect("profiles:show_self")

class EditCompanyProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_company_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        b = models.companyDetails.objects.filter(user=self.request.user).first()
        print b
        if "companyProfileForm" not in kwargs:
            kwargs["companyProfileForm"] = forms.companyProfileForm(instance=b)
        return super(EditCompanyProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwards):
        user = self.request.user
        b = models.companyDetails.objects.filter(user=user).first()
        print b
        companyProfileForm = forms.companyProfileForm(request.POST, instance=b)
        #b = models.companyDetails.objects.filter(user=self.request.user)
        #print b;
        companyProfile = companyProfileForm.save(commit=False)
        companyProfile.user = user
        companyProfile.save()

        if b is None:
            url = "https://lymosrv.ddns.net/lymousine/api/v1/thirdpartycompanysave"
            payload = {
                "company_name": request.post['companyName'],
                "company_address": request.post['address'],
                "zip_code": request.post['zipCode'],
                "phone_no": request.post['phone'],
                "trd_pty_usr": 1,
                "country": request.post['country'],
                "state": request.post['state'],
                "city": request.post['city'],
                "trd_party_user_type": request.post['userType'],
                }
            print payload
            response = requests.post(url, json = payload)
        else:
            url = "http://lymosrv.ddns.net/lymousine/api/v1/thirdpartycompanyupdate/"+user.email            
            payload = {
                "company_name": request.post['companyName'],
                "company_address": request.post['address'],
                "zip_code": request.post['zipCode'],
                "phone_no": request.post['phone'],
                "trd_pty_usr": 1,
                "country": request.post['country'],
                "state": request.post['state'],
                "city": request.post['city'],
                "trd_party_user_type": request.post['userType'],
                }
            print payload
            response = requests.post(url, json = payload)

        messages.success(request, "Company details has been saved!")
        return redirect("payments:addpayment")
        #return redirect("profiles:show_self")