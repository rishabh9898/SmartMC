from django import forms
from django.core import validators
from .models import SmartMC


class CreateForm(forms.ModelForm):
   export_to_CSV = forms.BooleanField(required=False)
   class Meta:
     model = SmartMC
     fields = ['name','pill_Box1','total_quantity','quantity','day_time','day_name']
# class Reg(forms.Form):
# 	name=forms.CharField(error_messages={'required':'Enter your name'})
# 	email=forms.CharField(error_messages={'required':'Enter your email'})
# 	password= forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Enter your password'})




