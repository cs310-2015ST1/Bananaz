from django.test import TestCase
from models import Garden
from models import User
from models import FoodTree

# Create your tests here.

class GardenMethodTests(TestCase):

    def test_ensure_latlong_are_positive(self):
        # ensure_latlong_are_positive should results True for Gardens where lat and long are zero or positive
                cat = Garden(latitude = -100,longitude=-1, name="TestGarden")
                cat.save()
                self.assertEqual((cat.latitude >= 0), True)
