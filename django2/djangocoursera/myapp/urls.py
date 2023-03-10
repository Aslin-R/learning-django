from django.urls import path 
from .import views
from django.urls import path,re_path

urlpatterns=[
    
    path('',views.intro,name='intro'),
    path('about/',views.about,name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('menu_card/',views.menu_by_id),
    path('menus/',views.menus,name='menus'),
    path('booking/', views.form_view),
    path('menu/<int:num>',views.menu,name='menu'),
    re_path(r'^menu/([0-9]{2})/$',views.menu),


     
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'), 

    path('about/',views.about),
    path('home/', views.home, name='home'),
    path('index/',views.index),
    path('base/',views.base),

]

