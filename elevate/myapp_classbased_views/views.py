from django.http import HttpResponse
from myapp.models import pwd_emp
from django.views.generic.edit import CreateView

# Create your views here.
def index_page_myapp_classbased_views(request):
    content = "<html><body><h1>Hello, world!</h1><h2>This is the Index Page view of myapp_classbased_views.</h2></body></html>"
    return HttpResponse(content)

class EmployeeCreate(CreateView):   
    model = pwd_emp    
    fields = '__all__' 
    success_url = "/myapp_classbased_views/success/" 