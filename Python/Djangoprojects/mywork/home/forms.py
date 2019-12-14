from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_password = forms.CharField(label='Password', max_length=32)
    your_contact = forms.CharField(label='Contact Number')
