from django.urls import path 
from .import views
from django.urls import path,re_path

urlpatterns=[
    path('home/',views.home,name='home'),
    
    path('getuser/', views.qryview, name='qryview') ,
    path("showform/", views.showform, name="showform"), 
    
    path('drinks/<str:drink_name>',views.drinks,name='drink_name'),
    path('menu/<int:num>',views.menu,name='menu'),
    re_path(r'^menu/([0-9]{2})/$',views.menu)

]

