from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import myform,dataform
from .models import mymodel


import datetime
# Create your views here.
def index(request):
	return HttpResponse("Hello welcome")

def askquestion(request,ques_id):
	return HttpResponse("asked question no. %s" % ques_id)

def intro(request):
	current_date_time = datetime.datetime.now()
	context = { 'now_date' : current_date_time }

	mymodel_obj = mymodel.objects.all()
	return render(request,'crudapp/hello.html',{'modeldata' : mymodel_obj})	

def getdata(request):

	if request.method=='POST':
		myform_detail = myform(request.POST)
	
		if myform_detail.is_valid():
			name_from_user = myform_detail.cleaned_data["name"]

			return HttpResponse("Form submitted succesfully by " + name_from_user)

	else:
		myform_detail = myform()
	return render(request,'crudapp/hello.html',{'form' : myform_detail})


def insertdata(request):

	if request.method == 'POST':
		dataform_obj = dataform(request.POST)

		if dataform_obj.is_valid():
			first_name_from_user = dataform_obj.cleaned_data['first_name']
			last_name_from_user = dataform_obj.cleaned_data['last_name']
			age_from_user = dataform_obj.cleaned_data['age']
			email_from_user = dataform_obj.cleaned_data['email']

			mymodel_obj = mymodel(first_name=first_name_from_user,last_name=last_name_from_user,age=age_from_user,email=email_from_user)
			mymodel_obj.save()

			return HttpResponse("Data inserted")

	else:
		dataform_obj = dataform()
		return render(request,'crudapp/insert.html',{'form':dataform_obj})

def updatedata(request,req_id):
	if request.method == 'POST':
		dataform_obj = dataform(request.POST)

		if dataform_obj.is_valid():
			modeldata = mymodel.objects.get(id=req_id)

			modeldata.first_name = dataform_obj.cleaned_data['first_name']
			modeldata.last_name = dataform_obj.cleaned_data['last_name']
			modeldata.age = dataform_obj.cleaned_data['age']
			modeldata.email = dataform_obj.cleaned_data['email']
			modeldata.save()
			

			return redirect("/crudapp/intro/")
	else:

		modeldata = mymodel.objects.get(id=req_id)
		dataform_obj = dataform(initial={'first_name':modeldata.first_name,'last_name':modeldata.last_name,'age':modeldata.age,'email':modeldata.email})
		return render(request,'crudapp/update.html', {'data':dataform_obj,'userid' : req_id})

def deletedata(request,req_id):
	modeldata = mymodel.objects.get(id=req_id)
	modeldata.delete()
	return redirect('/crudapp/intro/')