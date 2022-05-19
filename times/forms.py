from django import forms
from .models import TIME_OPTIONS

class AvailableTimeForm(forms.Form):
    times = forms.MultipleChoiceField(choices=TIME_OPTIONS)