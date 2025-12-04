from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ReservationForm
from .models import Reservation

# Homepage
def home(request):
    return render(request, "reservations/home.html")

def menu(request):
    return render(request, "reservations/menu.html")

def contact(request):
    return render(request, "reservations/contact.html")

@login_required
def book_reservation(request):
    existing_reservation = Reservation.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=existing_reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            if existing_reservation:
                messages.success(request, "Your reservation has been updated successfully!")
            else:
                messages.success(request, "Your reservation has been booked successfully!")
            return redirect("reservation_success", pk=reservation.pk)
        else:
            messages.error(request, "There was an error with your booking. Please try again.")
    else:
        form = ReservationForm(instance=existing_reservation)

    return render(request, "reservations/book_reservation.html", {
        "form": form,
        "existing_reservation": existing_reservation,
    })



# def reservation_success(request):
#     return render(request, "reservations/reservation_success.html")

def reservation_success(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservations/reservation_success.html', {'reservation': reservation})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created successfully!")
            return redirect("home")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "account/signup.html", {"form": form})

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, "reservations/my_reservations.html", {"reservations": reservations})

@login_required
def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated successfully!")
            return redirect("my_reservations")
    else:
        form = ReservationForm(instance=reservation)
    return render(request, "reservations/edit_reservation.html", {"form": form})

@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation cancelled successfully!")
        return redirect("my_reservations")
    return render(request, "reservations/delete_reservation.html", {"reservation": reservation})

# @login_required
# def manage_reservation(request, pk):
#     reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
#     form = ReservationForm(instance=reservation)
#     return render(request, "reservations/manage_reservation.html", {
#         "reservation": reservation,
#         "form": form,
#     })
@login_required
def manage_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated successfully!")
            return redirect("my_reservations")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ReservationForm(instance=reservation)

    return render(request, "reservations/manage_reservation.html", {
        "reservation": reservation,
        "form": form,
    })
