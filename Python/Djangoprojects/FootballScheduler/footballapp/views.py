from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from footballapp.forms import TeamForm,adminForm,LoginForm,updateGoal
from django.db import models
from footballapp.models import TeamModel,Schedules
from django.db import connection

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from itertools import permutations

def index(request):
	return render(request,"footballapp/index.html")

def teamRegister(request):
	team_count = TeamModel.objects.all().count()
	team_names = TeamModel.objects.values_list('TeamName', flat=True)
	team_list = list(team_names) 

	seq = permutations(team_list, 2)

	# team_seq = list(seq)


	# for p in list(seq):
	#    print(p)
	if team_count >= 10:
		return render(request,'footballapp/teamfixture.html',{'myseq' : list(seq)})

	elif request.method == 'POST':
		team_detail = TeamForm(request.POST)
		if team_detail.is_valid():

			team_name_user = team_detail.cleaned_data['TeamName']
			player_name1_user = team_detail.cleaned_data['Player1']
			player_name2_user = team_detail.cleaned_data['Player2']
			player_name3_user = team_detail.cleaned_data['Player3']
			player_name4_user = team_detail.cleaned_data['Player4']
			player_name5_user = team_detail.cleaned_data['Player5']
			player_name6_user = team_detail.cleaned_data['Player6']
			player_name7_user = team_detail.cleaned_data['Player7']
			player_name8_user = team_detail.cleaned_data['Player8']
			player_name9_user = team_detail.cleaned_data['Player9']
			player_name10_user = team_detail.cleaned_data['Player10']
			player_name11_user = team_detail.cleaned_data['Player11']
			coach_name_user = team_detail.cleaned_data['Coach']
			manager_name1_user = team_detail.cleaned_data['Manager1']
			manager_name2_user = team_detail.cleaned_data['Manager2']

			team_detail_object = TeamModel(TeamName=team_name_user,Player1=player_name1_user,Player2=player_name2_user,
				Player3=player_name3_user,Player4=player_name4_user,Player5=player_name5_user,
				Player6=player_name6_user,Player7=player_name7_user,Player8=player_name8_user,
				Player9=player_name9_user,Player10=player_name10_user,Player11=player_name11_user,
				Coach=coach_name_user,Manager1=manager_name1_user,Manager2=manager_name2_user)
			team_detail_object.save()

			return HttpResponse("Team Registered")

	else:
			team_detail = TeamForm()
			return render(request,'footballapp/registerteam.html',{'myform' : team_detail})

def adminRegister(request):

	if request.method == 'POST':
		admin_detail = adminForm(request.POST)
		if admin_detail.is_valid():

			username = admin_detail.cleaned_data['Username']	
			email = admin_detail.cleaned_data['EmailId']	
			password = admin_detail.cleaned_data['Password']	
			
			user = User.objects.create_user(username, email, password)
			user.save()
			user.is_active = False
			user.save()
				
			return HttpResponse('Admin Registered')
	else:
		admin_detail = adminForm()
		return render(request,'footballapp/registeradmin.html',{'myform' : admin_detail})

	
def adminLogin(request):

	if request.user.is_authenticated:
		return HttpResponse('You Are already logged in')
	else:	
		if request.method == 'POST':
			login_form = LoginForm(request.POST)
			if login_form.is_valid():

				username = login_form.cleaned_data['username']
				password = login_form.cleaned_data['password']

				user = authenticate(username=username, password=password)
				return HttpResponse('Log In succesfully')
							
				
			else:
				login_form = LoginForm()
				return render(request, "footballapp/login.html",{"myform":login_form})
		else:
			login_form = LoginForm()
			return render(request, "footballapp/login.html",{"myform":login_form})


def adminLogout(request):
    logout(request)
    return HttpResponse('Log Out succesfully')

def viewSquad(request):
    squad_detail = TeamModel.objects.all()
    context = {"squad":squad_detail}
    return render(request,'footballapp/viewsquad.html',context)
   

def viewFixture(request):
    schedule_detail = Schedules.objects.all()
    context = {"schedules":schedule_detail}
    return render(request,'footballapp/viewfixture.html',context)

def updateGoal(request,team_id):
	if request.method == "POST":
		update_form  = updateGoal(request.POST)

		if update_form.is_valid():
			schedule_detail = Schedules.objects.get(id=team_id)
			schedule_detail.Goalscore = update_form.cleaned_data['Goalscore']
			schedule_detail.save()

		return HttpResponseRedirect("/books/intro-page/")

	else:
		schedule_detail = Schedules.objects.get(id=team_id)
		update_form  = updateGoal(initial={"TeamName":schedule_detail.TeamName1,"Date":schedule_detail.Date,
			"Time":schedule_detail.Time,"Venue":schedule_detail.Venue,"Goalscore":schedule_detail.Goalscore})
		return render(request,'footballapp/updategoalscore.html',{'myform':update_form,'teamid':team_id})

def deleteGoalscore(request,team_id):
	goal_detail = Schedules.objects.get(id=team_id)
	goal_detail.delete()
	return HttpResponseRedirect("/footballapp/viewfixture/")