from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking
from .forms import BookingForm

# Create your views here.
def index_page_reservationform_little_lemon(request):
    content = "<html><body><h1>Hello, world!</h1><h2>This is the Index Page view of reservationform_little_lemon.</h2></body></html>"
    return HttpResponse(content)

def booking(request):       
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        guest_count = request.POST['guest_count']
        # reservation_time = request.POST['reservation_time'] # This cannot be used because its time saved automatically in models.py
        comments = request.POST['comments']
        booking = Booking(first_name=first_name,last_name=last_name,guest_count=guest_count,comments=comments)
        booking.save()

        return redirect('../booking')
    else:
        booking = BookingForm()
        context = {'booking': booking}
    return render(request, 'reservationform_little_lemon/booking.html', context)