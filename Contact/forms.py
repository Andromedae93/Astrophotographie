from django import forms
from .models import *


class ContactForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Contact
        fields = [
            'nom',
            'prenom',
            'description'
        ]
