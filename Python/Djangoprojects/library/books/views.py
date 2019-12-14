from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book_details
from books.forms import add_Books
from django import forms
from django.db import models

# Create your views here.

def pageFirst(request):
	book_detail = Book_details.objects.all()
	context = {"book":book_detail}
	return render(request,"books/intropage.html",context)	
	

def insertBooks(request):

	if request.method == 'POST':
		addbook_form = add_Books(request.POST)
		if addbook_form.is_valid():

			book_name_user = addbook_form.cleaned_data['book_name']
			author_name_user = addbook_form.cleaned_data['author_name']
			year_user = addbook_form.cleaned_data['year']

			book_detail_object = Book_details(book_name=book_name_user,author_name=author_name_user,year=year_user)
			book_detail_object.save()

			return HttpResponseRedirect("")

	else:
		addbook_form = add_Books()
		return render(request,'books/addbook.html',{'myform': addbook_form})

def viewBooks(request,book_id):
	book_detail = Book_details.objects.get(id=book_id)
	context = {"book" : book_detail}
	return render(request,'books/selectpage.html',context)

def editBooks(request,book_id):

	if request.method == "POST":
		
		book_form  = add_Books(request.POST)
		
		if book_form.is_valid():
			book_detail = Book_details.objects.get(id=book_id)
			book_detail.book_name = book_form.cleaned_data['book_name']
			book_detail.author_name = book_form.cleaned_data['author_name']
			book_detail.year = book_form.cleaned_data['year']
			book_detail.save()

		return HttpResponseRedirect("/books/intro-page/")

	else:

		book_detail = Book_details.objects.get(id=book_id)
		book_form  = add_Books(initial={"book_name":book_detail.book_name,
						"author_name":book_detail.author_name,"year":book_detail.year})
		return render(request,'books/editpage.html',{'form':book_form,'bookid':book_id})

def deleteBooks(request,book_id):
	book_detail = Book_details.objects.get(id=book_id)
	book_detail.delete()
	return HttpResponseRedirect("/books/intro-page/")