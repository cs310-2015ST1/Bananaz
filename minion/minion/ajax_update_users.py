from django.contrib.auth.models import User


from django.http import HttpResponse

from django.shortcuts import render

def import_user_data(request):
    users = User.objects.all()
    str = ''
    for u in users:
        str = str + u.username + "<br>"
    return HttpResponse(str)