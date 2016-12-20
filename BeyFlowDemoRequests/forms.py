from django.forms import ModelForm
from django import forms

from models import DemoRequest

class RequestDemoForm(ModelForm):
  
    class Meta:
        model = DemoRequest
        fields = ['firstName','lastName','email','jobTitle','workPhoneNumber','company','message','canReceiveMails']

