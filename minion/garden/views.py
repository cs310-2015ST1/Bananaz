from django.core.urlresolvers import reverse

from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth import logout as auth_logout
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

import oauth2 as oauth
import cgi
from twitter import *

from .models import Garden
from .models import FoodTree
from .forms import TweetForm
from .models import UserProfile


def index(request):
	food_types = generate_food_types()
	gardens = Garden.objects.order_by('name')
	return render_index(request, gardens, food_types, '')


# twitterauth
def logout(request):
	auth_logout(request)
	return redirect(reverse('index'))


def get_tweet(request):
	if request.method == 'POST':
		form = TweetForm(request.POST)
		current_user = request.user.userprofile
		if form.is_valid():
			tweet = form.cleaned_data['tweet']
			post_tweet(current_user,tweet)
	else:
		form = TweetForm()

	return render(request,'garden/form.html',{'form':form})

def post_tweet(user,tweet):
	t = Twitter(auth=OAuth(user.oauth_token,user.oauth_token_secret,'BVBOWynKxDOQkVLkVMUvxPXzY','A2iD5qZSGn3O0qiI3SbVd3nR7LQeHV5n4ikBQDMI7xZxf0ym8D'))
	t.statuses.update(status=tweet)


def render_index(request, gardens, food_types, food):
	return render(request, 'garden/index.html',
				{'gardens': gardens, 'food_types': food_types, 'name_of_fruit': food})


def generate_food_types():
	food_types = []
	all_trees = FoodTree.objects.order_by('food_type')

	for item in all_trees:
		if not (item.food_type in food_types):
			food_types.append(item.food_type)

	return food_types


def search_criteria(request):
	all_gardens = Garden.objects.order_by('name')

	food_types = generate_food_types()
	all_food_trees = FoodTree.objects.order_by('food_type')

	# Get / invalid Post request
	try:
		name_of_garden = request.POST['name']
		food = request.POST['foods']
	except MultiValueDictKeyError:
		return render_index(request, all_gardens, food_types, '')

	# empty search
	if ignore_name(name_of_garden) and ignore_foods(food):
		return render_index(request, all_gardens, food_types, food)

	elif ignore_name(name_of_garden):
		gardens = filter_by_foods(all_food_trees, food)

	elif ignore_foods(food):
		gardens = filter_by_name(all_gardens, name_of_garden)

	else:
		gardens = filter_by_foods(all_food_trees, food)
		gardens = filter_by_name(gardens, name_of_garden)


	return render_index(request, gardens, food_types, food)


def filter_by_name(gardens, name_of_garden):
	filtered_gardens = []
	for garden in gardens:
		if name_of_garden in garden.name:
			filtered_gardens.append(garden)
	return filtered_gardens


def filter_by_foods(all_food_trees, food):
	gardens = []
	for tree in all_food_trees:
		if tree.food_type in food:
			if tree.garden in gardens:
				pass
			else:
				gardens.append(tree.garden)
	return gardens


def ignore_name(name_of_garden):
	return name_of_garden == ''


def ignore_foods(list_of_foods):
	return (list_of_foods.__len__() == 0) or ("all" in list_of_foods)
