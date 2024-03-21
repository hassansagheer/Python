from django.urls import path 
from . import views 
from .views import EmployeeCreate

urlpatterns = [
    path('', views.index_genericviews, name='index_genericviews'),
    path('create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
]
