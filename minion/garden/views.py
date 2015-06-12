from django.shortcuts import render_to_response, redirect, render
from django.template.loader import render_to_string

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from django.template.context import RequestContext

from .models import Garden



# Create your views here.
def index(request):
	gardens = Garden.objects.order_by('name')
	return render(request,'garden/index.html',
			{'gardens' : gardens})


#twitterauth
def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')