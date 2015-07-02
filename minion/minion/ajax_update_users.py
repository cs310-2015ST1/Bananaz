__author__ = 'Haoran'
from django.http import HttpResponse
from garden.models import UserProfile

def import_user_data(request):
    return False