from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NameForm

# Create your views here.
'''
def login(request):
	return HttpResponse("Hello!!!")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    '''
import datetime

def index(request):
	current_datetime =datetime.datetime.now()
	content = {'now_date' : current_datetime}
	return render(request,'home/index.html',content)

def style(request):
	return render(request,'home/index.html')

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('Form submitted successfully<br>Name:'+ form.cleaned_data['your_name'])
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})
	