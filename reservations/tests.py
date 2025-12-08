from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Reservation
from .forms import ReservationForm

class ReservationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="andy", password="testpass")
        self.reservation = Reservation.objects.create(
            user=self.user,
            reservation_name="Andy Brookes",
            date="2025-12-25",
            time="19:00",
            party_size=2,
            email="andy@example.com"
        )

    def test_reservation_str(self):
        """Reservation __str__ should return reservation_name, date, and time"""
        expected_str = "Andy Brookes on 2025-12-25 at 19:00"
        self.assertEqual(str(self.reservation), expected_str)


# -------------------------
# View Tests
# -------------------------
class ReservationViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="andy", password="testpass")

    def test_home_page_loads(self):
        """Home page should return 200 and use correct template"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservations/home.html")  # <-- corrected template

    def test_reservation_page_requires_login(self):
        """Reservation page should redirect unauthenticated users to login"""
        response = self.client.get(reverse("book_reservation"))
        self.assertRedirects(response, f"{reverse('account_login')}?next={reverse('book_reservation')}")

    def test_reservation_page_authenticated(self):
        """Reservation page should load for logged-in users"""
        self.client.login(username="andy", password="testpass")
        response = self.client.get(reverse("book_reservation"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservations/book_reservation.html")


# -------------------------
# Form Tests
# -------------------------
class ReservationFormTest(TestCase):
    def test_valid_form(self):
        """Form should be valid with proper data"""
        form = ReservationForm(data={
            "reservation_name": "Andy Brookes",
            "date": "2025-12-25",
            "time": "19:00",
            "party_size": 2,
            "email": "andy@example.com"
        })
        self.assertTrue(form.is_valid(), msg=form.errors)  # show errors if it fails

    def test_invalid_form(self):
        """Form should be invalid with missing/incorrect data"""
        form = ReservationForm(data={
            "reservation_name": "",
            "date": "",
            "time": "",
            "party_size": 0,
            "email": ""  # required
        })
        self.assertFalse(form.is_valid())



        
