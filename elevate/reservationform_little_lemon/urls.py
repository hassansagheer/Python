from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page_reservationform_little_lemon, name='index_page_reservationform_little_lemon'),
    path('booking/', views.booking, name='booking'),
]