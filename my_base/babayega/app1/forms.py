from django import forms
from .models import PhoneContacts, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email_address', 'text')


class PhoneForm(forms.ModelForm):

    class Meta:
        model = PhoneContacts
        fields = ('network', 'phone_number')
