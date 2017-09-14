from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
import requests
import json


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
        try:
            if True:
                url = "https://lymosrv.ddns.net/lymousine/api/v1/thirdpartyusersave"
                payload = {
                    "name": user.name,
                    "email_id": user.email,
                    "mobile_no": request.POST['mobile'],
                    "bio": request.POST['bio']
                }
                print url
                print payload
                response = requests.post(url, json = payload)
                print response
                print response.text
                print type(response.text)
                data_to_store =json.loads(response.text)
                if data_to_store["success"]== True:
                    data_to_store_id = data_to_store["data"]["id"]
                    print data_to_store_id
                    print request.user.id
                    models.Profile.objects.filter(user=request.user.id).update(lymo_user_id=data_to_store_id)
                    print "updated"
                messages.success(request, "Profile details saved!")
                return redirect("dashboard")
        except Exception as e:
            print e
            print "error in api hitting"

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
        try:
            user = self.request.user
            b = models.companyDetails.objects.filter(user=user).first()
            print b
            companyProfileForm = forms.companyProfileForm(request.POST, instance=b)
            #b = models.companyDetails.objects.filter(user=self.request.user)
            #print b;
            companyProfile = companyProfileForm.save(commit=False)
            companyProfile.user = user
            companyProfile.save()
            profile_data=models.Profile.objects.filter(user=request.user.id).first()
            if profile_data is not None:            #
                lymo_profile_id= profile_data.lymo_user_id
            else:
                lymo_profile_id=None
            #print request.POST
            # if b is None:
            url = "https://lymosrv.ddns.net/lymousine/api/v1/thirdpartycompanysave"
            payload = {
                "company_name": request.POST['companyName'],
                "company_address": request.POST['address'],
                "zip_code": request.POST['zipCode'],
                "phone_no": request.POST['phone'],
                "trd_pty_usr": 1,
                "country": request.POST['country'],
                "state": request.POST['state'],
                "city": request.POST['city'],
                # "trd_party_user_type": request.POST['userType'],
                "trd_party_user_type":"company_secretary",
                "trd_pty_usr":lymo_profile_id,
                "created_by":lymo_profile_id,
                "updated_by":lymo_profile_id
                }
            print payload
            print url
            response = requests.post(url, json = payload)
            print response
            data_to_store =json.loads(response.text)
            print data_to_store
            print type(data_to_store["success"])
            if data_to_store["success"] == True:
                lymo_profile_id = data_to_store["data"]["trd_pty_usr"]
                lymo_company_id = data_to_store["data"]["id"]
                print lymo_profile_id
                print lymo_company_id
                data = models.companyDetails.objects.filter(user=user).update(lymo_profile_id=lymo_profile_id,lymo_company_id=lymo_company_id)
            print response.text  
            print response     
            messages.success(request, "Company details has been saved!")
            return redirect("payments:addpayment")
        except Exception as e:
            print e
        #return redirect("profiles:show_self")