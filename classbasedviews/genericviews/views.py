from django.http import HttpResponse
from .models import Employee
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.
def index_genericviews(request):
    content = "<html><body><h1 style='color:grey;'>Hello, world!</h1><h2>This is the Index Page view of genericviews app.</h2></body></html>"
    return HttpResponse(content)


class EmployeeCreate(CreateView):   
    model = Employee    
    fields = '__all__' 
    success_url = "/employees/success/"

class EmployeeList(ListView):   
    model = Employee   
    success_url = "/employees/success/" 