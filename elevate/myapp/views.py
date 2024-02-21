from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . models import pwd_emp

# Create your views here.
def index_page(request):
    content = "<html><body><h1>Hello, world!</h1><h2>This is the Index Page view of myapp.</h2></body></html>"
    return HttpResponse(content) 

def home_page(request):
    content = "<html><body><h1>Hello, world!</h1><h2>This is the Home Page view of myapp.</h2></body></html>"
    return HttpResponse(content) 

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def show_emp_data(request):
    emp_data = pwd_emp.objects.all()  # Retrieve all records
    # You can also filter data based on specific conditions:
    # emp_data = pwd_emp.objects.filter(office='Your Office Name')
    return render(request, 'myapp/show_emp_data.html', {'emp_data': emp_data})