from django import forms

CHOICES = [
  ('N', "NO; I have not taken all of the above steps/would not like to participate."),
  ('Y', "YES; I have taken all of the above steps and would like to participate."),
]

class RegisterForm(forms.Form):
    registered = forms.ChoiceField(label="Would you like to register?", choices=CHOICES, required=True)
    username = forms.CharField(max_length=255, label="Please enter your username to confirm.", required=True)