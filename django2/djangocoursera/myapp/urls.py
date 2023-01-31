from django.urls import path 
from .import views


urlpatterns=[
    path('home/',views.home,name='home'),
    path('getuser/', views.qryview, name='qryview') ,
    path("showform/", views.showform, name="showform"), 
    path('drinks/<str:drink_name>',views.drinks,name='drink_name')

]

