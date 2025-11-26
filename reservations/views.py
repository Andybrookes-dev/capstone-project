from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationForm



# def reservation_view(request):
#     return render(request, "reservations/reservation_view.html")

# Homepage
def home(request):
    return render(request, "reservations/home.html")

# Menu page
def menu(request):
    return render(request, "reservations/menu.html")

# Contact page
def contact(request):
    return render(request, "reservations/contact.html")

# Reservation landing page (optional, can remove if not needed)
def reservation_view(request):
    return render(request, "reservations/reservation_view.html")




def book_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.user = request.user
            reservation.save()
            messages.success(request, "Your reservation has been booked successfully!")
            return redirect("reservation_success")  # redirect to success page
        else:
            messages.error(request, "There was an error with your booking. Please try again.")
    else:
        form = ReservationForm()

    return render(request, "reservations/book_reservation.html", {"form": form})

def reservation_success(request):
    return render(request, "reservations/reservation_success.html")
