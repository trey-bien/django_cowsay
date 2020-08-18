from django import forms
from moo import models

class AddTextForm(forms.Form):
    text = forms.CharField(max_length=100)