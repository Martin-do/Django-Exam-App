from django import forms
from .models import *
class User_Option(forms.Form):
    opt = English19()
    CHOICES = [(opt.option1, opt.option1),(opt.option2, opt.option1)]
    option = forms.CharField(label=CHOICES, widget=forms.RadioSelect(choices=CHOICES))