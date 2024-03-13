from django.urls import path 
from .import views
from .views import EmployeeCreate

urlpatterns = [
    path('', views.index_page_myapp_classbased_views, name='index_page_myapp_classbased_views'),
    path('create/', EmployeeCreate.as_view(), name = 'EmployeeCreate') ,
]