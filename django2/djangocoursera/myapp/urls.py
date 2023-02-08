from django.urls import path 
from .import views
from django.urls import path,re_path

urlpatterns=[
    
    path('',views.intro,name='intro'),
    path('contact/', views.contact_view, name='contact'),
    path('forms/', views.form_view),
    path('getuser/', views.qryview, name='qryview') ,
    path('drinks/<str:drink_name>',views.drinks,name='drink_name'),
    path('menu/<int:num>',views.menu,name='menu'),
    re_path(r'^menu/([0-9]{2})/$',views.menu)

]

