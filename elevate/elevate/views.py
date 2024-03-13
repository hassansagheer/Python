from django.http import HttpResponse

# Create your views here.
def index_page_elevate(request):
    content = "<html><body><h1>Hello, world!</h1><h2>This is the Index Page view of elevate project.</h2></body></html>"
    return HttpResponse(content)