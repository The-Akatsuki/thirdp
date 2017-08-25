from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            )

    class Meta:
        model = User
        fields = ['name']


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            Field('bio'),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.Profile
        fields = ['picture', 'bio']


class companyProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(companyProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('companyName',css_class="companyName"),
            Field('phone', css_class="phone"),
            Field('address', css_class="address"),
            Field('city', css_class="city"),
            Field('state', css_class="state"),
            Field('country', css_class="country"),
            Field('zipCode', css_class="zipCode"),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.companyDetails
        fields = ['companyName', 'phone', 'address', 'city', 'state', 'zipCode', 'country']
