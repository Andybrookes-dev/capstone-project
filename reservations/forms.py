from django import forms
from .models import Reservation
import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "email", "phone", "date", "time", "party_size", "special_requests"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }

    def clean_time(self):
        time = self.cleaned_data.get("time")
        if time:
            import datetime
            start = datetime.time(12, 0)
            end = datetime.time(22, 0)
            if not (start <= time <= end):
                raise forms.ValidationError(
                    "Reservations can only be made between 12:00 PM and 10:00 PM."
                )
        return time