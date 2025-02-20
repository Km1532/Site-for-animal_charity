from django.contrib import admin
from django.urls import path
from donations import views  
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('animals/', views.animals_list, name='animals_list'),
    path('adopt/<int:id>/', views.adopt, name='adopt'), 
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
