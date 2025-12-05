from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Reservation(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    reservation_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)])
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=False)
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reservation_name} on {self.date} at {self.time}"
    
