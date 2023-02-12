from django.test import TestCase
from datetime import datetime
from .models import Booking

class BookingModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.booking=Booking.objects.create(first_name='John',last_name='t',reservation_time='12:00')

    def test_fields(self):
        self.assertIsInstance(self.booking.first_name,str)
        self.assertIsInstance(self.booking.last_name,str)

    def test_timestamps(self):
        self.assertIsInstance(self.booking.reservation_time,datetime)
        
        









