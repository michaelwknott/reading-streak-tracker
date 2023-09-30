from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    # Hide the email field. The user's email is not required for Signup
    email = forms.CharField(widget=forms.HiddenInput(), required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.email = ""  # Set email to an empty string as default value
        user.save()
        return user
