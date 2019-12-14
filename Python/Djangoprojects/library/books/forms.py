from django import forms

class add_Books(forms.Form):
	book_name = forms.CharField(label="Book Name")
	author_name = forms.CharField(label="Author Name")
	year = forms.IntegerField(label="Published Year")