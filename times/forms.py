from django import forms
from .utils import TIME_OPTIONS

class AvailableTimeForm(forms.Form):
    times = forms.MultipleChoiceField(choices=TIME_OPTIONS, required=False, widget=forms.CheckboxSelectMultiple)