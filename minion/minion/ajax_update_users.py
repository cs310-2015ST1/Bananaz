__author__ = 'Haoran'
from django.http import HttpResponse
from garden.models import UserProfile
from django.shortcuts import render

def import_user_data(request):
    users = UserProfile.objects.all()
    #return HttpResponse({'users': users})
    return render(request, 'garden/index.html',
				{'users': users})