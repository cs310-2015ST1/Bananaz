from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.utils.datastructures import MultiValueDictKeyError
from twitter import *
from minion.settings import SOCIAL_AUTH_TWITTER_SECRET, SOCIAL_AUTH_TWITTER_KEY

from .models import Garden

from .models import FoodTree
from .forms import TweetForm


def index(request):
	food_types = generate_food_types()
	gardens = Garden.objects.order_by('name')
	return render_index(request, gardens, food_types, 'any', '')


# twitterauth
def logout(request):
	auth_logout(request)
	return redirect(reverse('index'))


def get_tweet(request):
	if request.method == 'POST':
		form = TweetForm(request.POST)
		current_user = request.user.userprofile
		tweet = request.POST['Tweet']
		post_tweet(current_user,tweet)
	else:
		form = TweetForm()

	return redirect(reverse('index'))

def post_tweet(user, tweet):
	t = Twitter(auth=OAuth(user.oauth_token, user.oauth_token_secret, SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET))
	t.statuses.update(status=tweet)
	search_term = request.POST['search_term']
	tweets = t.search.tweets(q=search_term)

def search_tweets(request):
	current_user = request.user.userprofile
	t = Twitter(auth=OAuth(user.oauth_token,user.oauth_token_secret,SOCIAL_AUTH_TWITTER_KEY,SOCIAL_AUTH_TWITTER_SECRET))

def render_index(request, gardens, food_types, food, name_of_garden):
	return render(request, 'garden/index.html',
				{'gardens': gardens, 'food_types': food_types, 'name_of_fruit': food, 'name_of_garden': name_of_garden})


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
		return render_index(request, all_gardens, food_types, 'any', '')

	# empty search
	if ignore_name(name_of_garden) and ignore_foods(food):
		return render_index(request, all_gardens, food_types, 'any', name_of_garden)

	elif ignore_name(name_of_garden):
		gardens = filter_by_foods(all_food_trees, food)

	elif ignore_foods(food):
		gardens = filter_by_name(all_gardens, name_of_garden)
		food = 'any'

	else:
		gardens = filter_by_foods(all_food_trees, food)
		gardens = filter_by_name(gardens, name_of_garden)


	return render_index(request, gardens, food_types, food, name_of_garden)


def filter_by_name(gardens, name_of_garden):
	filtered_gardens = []
	for garden in gardens:
		if name_of_garden.lower() in (garden.name).lower():
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


def save_garden(request):
	garden_id = request.POST['garden_id']
	set_saved = request.POST['set_saved'].lower() == 'true'
	garden = get_object_or_404(Garden, id=garden_id)
	is_garden_saved = request.user.userprofile.gardens.filter(id=garden_id).exists()

	if set_saved and not is_garden_saved:
		request.user.userprofile.gardens.add(garden)
	elif not set_saved and is_garden_saved:
		request.user.userprofile.gardens.remove(garden)

	return HttpResponse("Success!")
