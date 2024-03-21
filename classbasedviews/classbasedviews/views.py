from django.http import HttpResponse

# Create your views here.
def index(request):
    content = "<html><body><h1 style='color:green;'>Hello, world!</h1><h2>This is the Index Page view of classbasedviews project.</h2></body></html>"
    return HttpResponse(content)