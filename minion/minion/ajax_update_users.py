from garden.models import UserProfile

from django.http import HttpResponse


def import_user_data(request):
    users = UserProfile.objects.all()
    str = ''
    for u in users:
        str = str + u.__str__() + "<br>"
    return HttpResponse(str)