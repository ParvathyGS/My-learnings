from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm,BlogForm
from .models import Blog

from django.core.paginator import Paginator

def index(request):
	return HttpResponse("Hello Parvathy...!!")

def display(request):
	return render(request,'branch/display.html')

def namedisp(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponse('Form submitted successfully<br>Name:'+form.cleaned_data['your_name'])
	else:
		form = NameForm()
	return render(request, 'branch/name.html', {'form': form})

def modeldisp(request):
	if request.method == 'POST':
		blog_form = BlogForm(request.POST)
		if blog_form.is_valid():
			blog_name_user = blog_form.cleaned_data['blog_name']
			blog_tag_line_user = blog_form.cleaned_data['blog_tag_line']

		blog_obj = Blog(name=blog_name_user,tagline=blog_tag_line_user)
		blog_obj.save()

		return HttpResponse('Data Inserted successfully')

	else:
		blg_form = BlogForm()

		return render(request,'branch/model_disp.html',{'form' : blg_form})

def select(request,requested_id):
	blog_obj = Blog.objects.get(id=requested_id)
	return render(request,'branch/select.html',{'blogdata' : blog_obj})

def update(request,requested_id):
	if request.method == 'POST':
		blog_form = BlogForm(request.POST)
		if blog_form.is_valid():
			 blog_obj = Blog.objects.get(id=requested_id)
			 blog_obj.name = blog_form.cleaned_data['blog_name']
			 blog_obj.tagline = blog_form.cleaned_data['blog_tag_line']
			 blog_obj.save()
		return HttpResponse('Updated')

	else:
		blog_obj = Blog.objects.get(id=requested_id)
		blog_form = BlogForm(initial={'blog_name':blog_obj.name,'blog_tag_line':blog_obj.tagline})

		return render(request,'branch/update.html',{'blogform' : blog_form,'blog_id' : requested_id})

def delete(request,requested_id):
	blog_obj = Blog.objects.get(id=requested_id)
	blog_obj.delete()
	return HttpResponse("deleted data")

def pag(request):
	blog_list = Blog.objects.all()
	paginator = Paginator(blog_list,2)
	page = request.GET.get('page')
	blogs = paginator.get_page(page)

	return render(request, "branch/list-blogs.html",{"blogs":blogs})

