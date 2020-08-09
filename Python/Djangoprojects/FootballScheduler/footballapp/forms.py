from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TeamForm(forms.Form):

	TeamName = forms.CharField(label="Team Name")
	Player1 = forms.CharField(label="Player Name - 1")
	Player2 = forms.CharField(label="Player Name - 2")
	Player3 = forms.CharField(label="Player Name - 3")
	Player4 = forms.CharField(label="Player Name - 4")
	Player5 = forms.CharField(label="Player Name - 5")
	Player6 = forms.CharField(label="Player Name - 6")
	Player7 = forms.CharField(label="Player Name - 7")
	Player8 = forms.CharField(label="Player Name - 8")
	Player9 = forms.CharField(label="Player Name - 9")
	Player10 = forms.CharField(label="Player Name - 10")
	Player11 = forms.CharField(label="Player Name - 11")
	Coach = forms.CharField(label="Coach Name")
	Manager1 = forms.CharField(label="Manager Name - 1")
	Manager2 = forms.CharField(label="Manager Name - 2")

class adminForm(forms.Form):

	Username = forms.CharField(label="User Name")
	EmailId = forms.EmailField(max_length=200, help_text='Required')
	Password = forms.CharField(widget=forms.PasswordInput(),label="Password")

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

class updateGoal(forms.Form):
	TeamName =  forms.CharField(label="Team Name")
	Date = forms.DateField()
	Time = forms.DateTimeField()
	Venue = forms.CharField(label="venue")
	Goalscore = forms.CharField(label="Goalscore")