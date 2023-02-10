from django.urls import path 
from .import views
from django.urls import path,re_path

urlpatterns=[
    
    path('',views.intro,name='intro'),
    path('about/',views.about,name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('menus/',views.menus,name='menus'),
    path('booking/', views.form_view),
    path('menu/<int:num>',views.menu,name='menu'),
    re_path(r'^menu/([0-9]{2})/$',views.menu)

]

