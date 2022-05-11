from django import forms

class RegisterForm(forms.Form):
    CHOICES = [
      ('N', "NO; Incomplete/Unavailable (default)"),
      ('Y', "YES; I did as above"),
    ]
    QUESTION = """
Are you sure you want to register? By selecting \"YES,\", you confirm that you
have followed all of the above instructions and are available for contest
participation.
    """
    registered = forms.ChoiceField(label=QUESTION, choices=CHOICES, required=True)
    username = forms.CharField(max_length=255, label="Please enter your username to confirm.", required=True)