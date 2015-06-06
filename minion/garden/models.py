from django.db import models

# Because Django requires these
MAX_LENGTH = 255
DECIMAL_PLACES = 20
MAX_DIGITS = 20

class Garden(models.Model):
    latitude = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    longitude = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    name = models.CharField(max_length=MAX_LENGTH)

class FoodTree(models.Model):
    garden = models.ForeignKey(Garden)
    amount = models.IntegerField()
    food_type = models.CharField(max_length=MAX_LENGTH)

class User(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
