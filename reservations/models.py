from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    """
    Stores a single reservation entry for a restaurant.
    Linked optionally to a registered user.
    """

    # If you want to tie reservations to logged-in users
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="reservations"
    )

    name = models.CharField(max_length=100)  # Guest name
    email = models.EmailField()              # Contact email
    phone = models.CharField(max_length=20, blank=True)  # Optional phone number

    date = models.DateField()                # Reservation date
    time = models.TimeField()                # Reservation time
    party_size = models.PositiveIntegerField()  # Number of guests

    special_requests = models.TextField(blank=True)  # Dietary needs, seating preferences, etc.

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
        return f"Reservation for {self.name} on {self.date} at {self.time}"



