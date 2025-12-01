from django.db import models
from django.contrib.auth.models import User



class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reservation_name} on {self.date} at {self.time}"
    
