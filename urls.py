"""
URL configuration for eproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_page,name='register'),
    path('login/', views.login_page, name='login'),
    path('', views.home_page ,name='home'), 
    path('logout/', views.logout_page,name='logout'),
    path('collection/', views.collections,name='collection'),
   path('collections/<slug:name>/', views.collectionsview, name='collections'),
   path('product_details/<slug:cat_name>/<slug:pro_name>/',views.product_details,name='product_details'),
  
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)