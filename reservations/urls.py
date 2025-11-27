from django.urls import path
from . import views

urlpatterns = [
    # Core pages
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("contact/", views.contact, name="contact"),

    # Reservation flow
    path("book/", views.book_reservation, name="book_reservation"),
    path("success/", views.reservation_success, name="reservation_success"),

    # Reservation CRUD
    path("reservations/", views.my_reservations, name="my_reservations"),
    path("reservations/<int:pk>/edit/", views.edit_reservation, name="edit_reservation"),
    path("reservations/<int:pk>/delete/", views.delete_reservation, name="delete_reservation"),

    # Authentication
    path("signup/", views.signup, name="signup"),
]
