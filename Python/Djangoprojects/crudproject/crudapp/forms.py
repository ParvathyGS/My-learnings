from django import forms

class myform(forms.Form):
	name = forms.CharField(max_length=20,label='Your name')

class dataform(forms.Form):
	first_name = forms.CharField(max_length = 50,label='First name')
	last_name = forms.CharField(max_length = 50,label='Last name')
	age = forms.IntegerField(label='Age')
	email = forms.EmailField(label='Email ID')