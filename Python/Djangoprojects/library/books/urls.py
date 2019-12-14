from django.urls import path
from . import views

urlpatterns = [
	path('intro-page/',views.pageFirst,name = 'pageFirst'),
	path('addbooks/',views.insertBooks,name = 'insertBooks'),
	path('viewbooks/<int:book_id>/',views.viewBooks,name = 'viewBooks'),
	path('editbooks/<int:book_id>/',views.editBooks,name = 'editBooks'),
	path('deletebooks/<int:book_id>/',views.deleteBooks,name = 'deleteBooks'),
	]