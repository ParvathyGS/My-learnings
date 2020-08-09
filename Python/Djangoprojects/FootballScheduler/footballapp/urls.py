from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('',views.index,name ='index'),
	path('teamregister/',views.teamRegister,name ='teamRegister'),
	path('adminregister/',views.adminRegister,name ='adminRegister'),
	path('adminlogin/',views.adminLogin,name ='adminLogin'),
	path('adminlogout/',views.adminLogout,name ='adminLogout'),
	path('viewsquad/',views.viewSquad,name ='viewSquad'),
	path('viewfixture/',views.viewFixture,name ='viewFixture'),
	# path('matches/',views.fixtures,name ='fixtures'),
	path('updategoal/<int:team_id>/',views.updateGoal,name ='updateGoal'),
	path('delete/<int:team_id>/',views.deleteGoalscore,name ='deleteGoalscore'),
	]