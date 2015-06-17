from django.contrib.auth.models import User
from django.db import models
#from django.db.models.signals import post_save

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

#twitterauth
# class Account(models.Model):
# 	name = models.CharField(max_length=120, default= '', blank=False, null=True)
# 	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
# 	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
# 	def __str__(self):
# 		return self.name

#twitterprofile
class UserProfile(models.Model):
    user = models.OneToOneField(User, null = True)
    photo = models.TextField()
profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def __str__(self):
    return self.user.username


# def user_post_save(sender, instance, created, **kwargs):
#     """Create a user profile when a new user account is created"""
#     if created == True:
#         p = UserProfile()
#         p.account = instance
#         p.save()

# post_save.connect(user_post_save, sender=User)