from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    """
    Represents a physical table in the restaurant.
    """
    number = models.IntegerField(unique=True)  # Table number
    capacity = models.PositiveIntegerField()   # How many guests can sit here
    location = models.CharField(max_length=100)  # e.g. "Patio", "Main Hall"

    def __str__(self):
        return f"Table {self.number} ({self.capacity} seats - {self.location})"


class Reservation(models.Model):
    """
    Stores a single reservation entry for a restaurant.
    Linked optionally to a registered user and a table.
    """

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="reservations"
    )
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="reservations",
        null=True,        # allow nulls temporarily
        blank=True        # allow blank in forms
    )

    name = models.CharField(max_length=100)  
    email = models.EmailField()              
    phone = models.CharField(max_length=20, blank=True)  

    date = models.DateField()                
    time = models.TimeField()                
    party_size = models.PositiveIntegerField()  

    special_requests = models.TextField(blank=True)  

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending"
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-time"]

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time} (Table {self.table.number})"
