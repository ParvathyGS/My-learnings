from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def site(request):
	return HttpResponse("Yipeee!!! My second successfull app in Django")
