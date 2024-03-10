from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking
from .forms import BookingForm

# Create your views here.
def booking(request):       
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        guest_count = request.POST['guest_count']
        reservation_time = request.POST['reservation_time']
        comments = request.POST['comments']
        booking = Booking(first_name=first_name,last_name=last_name,guest_count=guest_count,reservation_time=reservation_time,comments=comments)
        booking.save()

        return redirect('../booking')
    else:
        booking = BookingForm()
        context = {'booking': booking}
    return render(request, 'reservationform_little_lemon/booking.html', context)