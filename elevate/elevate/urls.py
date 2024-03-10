"""
URL configuration for elevate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin 
# from django.urls import include, path 

# urlpatterns = [ 
#     path('index_page/', include('myapp.urls')),
#     path('home_page/', include('myapp.urls')),
#     path('show_emp_data/', include('myapp.urls')),
#     path('admin/', admin.site.urls), 
# ] 

# ========================================================== #

from django.contrib import admin 
from django.urls import path 
from myapp import views
from reservationform_little_lemon import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_page/', views.index_page, name='index_page'),
    path('home_page/', views.home_page, name='home_page'),
    path('display_date/', views.display_date, name='display_date'),
    path('show_emp_data/', views.show_emp_data, name='show_emp_data'),
    path('insert_emp_data/', views.insert_emp_data, name='insert_emp_data'),
    path('delete_emp_data/<int:pk>', views.delete_emp_data, name='delete_emp_data'),
    path('update_emp_data/<int:pk>', views.update_emp_data, name='update_emp_data'),
    path('form/', views.form, name='form'),
    # path('booking/', views.booking, name='booking'),
]
