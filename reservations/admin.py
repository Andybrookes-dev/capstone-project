from django.contrib import admin
from .models import Reservation



@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("reservation_name", "date", "time", "party_size")
    list_filter = ("date",)

