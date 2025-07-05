from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.
def index(request):
    data = {
        "flights":Flight.objects.all(),
    }
    return render(request, "flights/index.html",data)

def flight(request, flight_id):
    # flight = Flight.objects.get(id=flight_id)
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request,"flights/flights.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    })


def book(request,flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))

        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("flights", args=(flight.id)))

