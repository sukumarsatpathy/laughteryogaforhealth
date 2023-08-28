from django import forms
from .models import Contact, Invite, Newsletter


class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullName', 'email', 'message']


class inviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['fullName', 'email', 'contact', 'country', 'message']


class newsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email',]
