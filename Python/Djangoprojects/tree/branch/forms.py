from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name',max_length=100)

#...    
class BlogForm(forms.Form):
    blog_name = forms.CharField(label='Blog Name')  
    blog_tag_line = forms.CharField(label='Blog Tagline')   
#...    
