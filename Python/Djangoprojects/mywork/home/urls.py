from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index, name = 'index'),
	path('style/', views.style, name = 'style'),
	path('parvathy/', views.get_name, name = 'get_name')
	#path('login/', views.login, name = 'login'),
	#path('<int:question_id>/detail/', views.detail, name = 'detail'),
	#path('<int:question_id>/hello/', views.results, name = 'results'),
	#path('<int:question_id>/vote/', views.vote, name = 'vote'),
	]
