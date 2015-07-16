from garden.models import UserProfile

from django.http import HttpResponse


def import_user_data(request):
    users = UserProfile.objects.all()
    str = '<table> <tr> <th>Username</th> <th>Name</th> <th>Email</th></tr>'
    for u in users:
        str = str + u.__str__() + "<br>"
    str = str + '</table>'
    return HttpResponse(str)