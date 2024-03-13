from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index_page_myapp, name='index_page_myapp'),
    path('home_page/', views.home_page, name='home_page'),
    path('display_date/', views.display_date, name='display_date'),
    path('show_emp_data/', views.show_emp_data, name='show_emp_data'),
    path('insert_emp_data/', views.insert_emp_data, name='insert_emp_data'),
    path('delete_emp_data/<int:pk>', views.delete_emp_data, name='delete_emp_data'),
    path('update_emp_data/<int:pk>', views.update_emp_data, name='update_emp_data'),
    path('form/', views.form, name='form'),
]