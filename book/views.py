from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def booker(request):
    return HttpResponse("This is where you'll make bookings!")