from django.contrib.auth.models import User
from django.db import models

# Because Django requires these
MAX_LENGTH = 255
DECIMAL_PLACES = 7
MAX_DIGITS = DECIMAL_PLACES + 3  # For decimals, integer-part has max size of MAX_DIGITS - DECIMAL_PLACES

class Garden(models.Model):
    latitude = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    longitude = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    name = models.CharField(max_length=MAX_LENGTH)

class FoodTree(models.Model):
    garden = models.ForeignKey(Garden)
    amount = models.IntegerField()
    food_type = models.CharField(max_length=MAX_LENGTH)

#twitterprofile
class UserProfile(models.Model):
    user = models.OneToOneField(User, null = True)
    oauth_token = models.TextField()
    oauth_token_secret = models.TextField()
    photo = models.TextField()

    def __str__(self):
        if (self.user.email):
            email = 'email: ' + self.user.email
        else:
            email = ''

        return 'username: ' + self.user.username + '<br>' + 'Name: ' + self.user.first_name + ' ' + self.user.last_name + '<br>' + email + '<br>'

