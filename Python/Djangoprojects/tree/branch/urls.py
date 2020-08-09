from django.urls import path
from . import views

urlpatterns = [
path('',views.index,name='index'),
path('display/',views.display,name='display'),
path('name/',views.namedisp,name='namedisp'),
path('insert/',views.modeldisp,name='modeldisp'),
path('<int:requested_id>/select/',views.select,name='select'),
path('<int:requested_id>/update/',views.update,name='update'),
path('<int:requested_id>/delete/',views.delete,name='delete'),
path('page/',views.pag,name='pag'),
]