from django import forms

class SubscriptionForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=254)