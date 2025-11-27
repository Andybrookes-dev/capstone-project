# from django.urls import path
# from . views import reservation_view

# urlpatterns = [
#     path('', reservation_view, name='reservation'),
# ]

from django.urls import path
from .views import reservation_view, book_reservation, reservation_success
from . import views

urlpatterns = [
    path("", reservation_view, name="reservation"),
    # path("book/", book_reservation, name="book_reservation"),
    # path("success/", reservation_success, name="reservation_success"),
    path("", views.home, name="home"), 
    path("menu/", views.menu, name="menu"),
    path("book/", views.book_reservation, name="book_reservation"),
    path("contact/", views.contact, name="contact"),
    path("success/", views.reservation_success, name="reservation_success"),
]
