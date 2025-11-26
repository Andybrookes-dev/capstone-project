from django.contrib import admin
from .models import Table, Reservation
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("number", "capacity", "location")
    search_fields = ("number", "location")
    list_filter = ("capacity",)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "time", "party_size", "status", "table", "user")
    search_fields = ("name", "email", "phone")
    list_filter = ("status", "date", "table")
    readonly_fields = ("created_on", "updated_on")