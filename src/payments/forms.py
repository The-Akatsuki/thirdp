from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

class paymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(paymentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('nameOnCard', css_class="nameOnCard"),
            Field('cardNumber', css_class="cardNumber"),
            Field('expirationDateMM', css_class="expirationDateMM col-md-3"),
            Field('expirationDateYY', css_class="expirationDateYY col-md-4"),
            Field('cvcCode',  widget=PasswordInput, css_class="cvcCode col-md-6"),
            Field('address', css_class="address"),
            Field('city', css_class="city col-md-6"),
            Field('state', css_class="state col-md-6"),
            Field('zipCode', css_class="zipCode col-md-6"),
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.paymentsDetails
        fields = ['nameOnCard', 'cardNumber', 'expirationDateMM', 'expirationDateYY', 'cvcCode',  'address', 'city', 'state', 'zipCode']
