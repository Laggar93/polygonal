from django import forms

class form_contact(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    comment = forms.CharField(required=True)