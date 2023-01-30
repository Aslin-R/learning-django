from django.urls import path 
from .import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('aslin/',views.aslin,name='aslin'),
    path('getuser/', views.qryview, name='qryview') ,
    path("showform/", views.showform, name="showform"), 
    path('dishes/<str:dish>',views.menuitems)

]

