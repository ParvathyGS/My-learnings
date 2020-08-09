from django.urls import path
from . import views

urlpatterns = [
path('index/',views.index,name='index'),
path('askquestion/<int:ques_id>/',views.askquestion,name='askquestion'),
path('intro/',views.intro,name='intro'),
path('getdata/',views.getdata,name='getdata'),
path('insertdata/',views.insertdata,name='insertdata'),
path('updatedata/<int:req_id>/',views.updatedata,name='updatedata'),
path('deletedata/<int:req_id>/',views.deletedata,name='deletedata'),
]