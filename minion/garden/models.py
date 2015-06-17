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

class User(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return self.name

#twitterauth
class Account(models.Model):
	name = models.CharField(max_length=120, default= '', blank=False, null=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	def __str__(self):
		return self.name

#twitterprofile
class Profile(models.Model):
	user = models.ForeignKey(User)
	oauth_token = models.CharField(max_length=200)
	oauth_secret = models.CharField(max_length=200)
