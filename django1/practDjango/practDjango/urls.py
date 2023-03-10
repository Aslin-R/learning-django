from django.contrib import admin 
from django.urls import include, path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('demo/', include('demoapp.urls')), 
    path('admin/', admin.site.urls), 
    path('travello', include('travello.urls')),
    path('account/', include('account.urls')), 

] 
urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)