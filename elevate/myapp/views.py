from django.shortcuts import render, redirect
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

# Show Employee
def show_emp_data(request):
    emp_data = pwd_emp.objects.all()  # Retrieve all records
    return render(request, 'myapp/show_emp_data.html', {'emp_data': emp_data})

# Insert Employee
def insert_emp_data(request):
    if request.method == "POST":
        emp_id = request.POST['emp_id']
        emp_name = request.POST['emp_name']
        emp_cnic = request.POST['emp_cnic']
        office = request.POST['office']
        emp_data = pwd_emp(emp_id=emp_id, emp_name=emp_name, emp_cnic=emp_cnic, office=office)
        emp_data.save()
  
        return redirect('../show_emp_data')
    else:
        return render(request, 'myapp/insert_emp_data.html')
    
# Update Employee
def update_emp_data(request,pk):
    emp_data = pwd_emp.objects.get(emp_id=pk)
    if request.method == 'POST':
            print(request.POST)
            emp_data.emp_id = request.POST['emp_id']
            emp_data.emp_name = request.POST['emp_name']
            emp_data.emp_cnic = request.POST['emp_cnic']
            emp_data.office = request.POST['office']
            emp_data.save()
            return redirect('../show_emp_data')
    context = {
        'emp_data': emp_data,
    }

    return render(request,'myapp/update_emp_data.html',context)

# Delete Employee
def delete_emp_data(request, pk):
    emp_data = pwd_emp.objects.get(emp_id=pk)

    if request.method == 'POST':
        emp_data.delete()
        return redirect('../show_emp_data')

    context = {
        'emp_data': emp_data,
    }

    return render(request, 'myapp/delete_emp_data.html', context)
