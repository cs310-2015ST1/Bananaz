from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.utils.datastructures import MultiValueDictKeyError
from twitter import *

from minion.settings import SOCIAL_AUTH_TWITTER_SECRET, SOCIAL_AUTH_TWITTER_KEY
from .models import Garden, GardenUserRelationship
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

def search_tweets(request, search_term):
	current_user = request.user.userprofile
	t = Twitter(auth=OAuth(current_user.oauth_token,current_user.oauth_token_secret,SOCIAL_AUTH_TWITTER_KEY,SOCIAL_AUTH_TWITTER_SECRET))
	tweets = t.search.tweets(q="#"+search_term)
	
	return render(request, 'garden/view_tweets.html', {'tweets':tweets})

def render_index(request, gardens, food_types, food, name_of_garden):
	if request.user.is_authenticated() and not request.user.is_superuser:
		saved_gardens = gardens.filter(gardenuserrelationship__userprofile=request.user.userprofile)
		saved_gardens = sorted(
			saved_gardens,
			key=lambda garden: garden.gardenuserrelationship_set.get(userprofile=request.user.userprofile).date_saved,
			reverse=True
		)
		unsaved_gardens = gardens.exclude(gardenuserrelationship__userprofile=request.user.userprofile).order_by('name')
		ordered_gardens = saved_gardens + list(unsaved_gardens)
	else:
		ordered_gardens = gardens.order_by('name')

	return render(request, 'garden/index.html', {
		'gardens': ordered_gardens,
		'food_types': food_types,
		'name_of_fruit': food,
		'name_of_garden': name_of_garden
	})


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
		return render_index(request, all_gardens, food_types, 'any', '')

	elif ignore_name(name_of_garden):
		gardens = filter_by_foods(all_food_trees, food)
		name_of_garden = ''

	elif ignore_foods(food):
		gardens = filter_by_name(all_gardens, name_of_garden)
		food = 'any'

	else:
		gardens = filter_by_foods(all_food_trees, food)
		gardens = filter_by_name(gardens, name_of_garden)


	return render_index(request, gardens, food_types, food, name_of_garden)


def filter_by_name(gardens, name_of_garden):
	return gardens.filter(name__icontains=name_of_garden)


def filter_by_foods(all_food_trees, food):
	return Garden.objects.filter(foodtree__food_type__icontains=food)


def ignore_name(name_of_garden):
	return (name_of_garden == '') or (name_of_garden == "Type Keyword in the Name of the Garden (leave blank to list all)")


def ignore_foods(list_of_foods):
	return (list_of_foods.__len__() == 0) or ("all" in list_of_foods)


def save_garden(request):
	set_saved = request.POST['set_saved'].lower() == 'true'
	garden = get_object_or_404(Garden, id=request.POST['garden_id'])
	is_garden_saved = GardenUserRelationship.objects.filter(userprofile=request.user.userprofile, garden=garden).exists()

	if set_saved and not is_garden_saved:
		GardenUserRelationship.objects.create(userprofile=request.user.userprofile, garden=garden)
	elif not set_saved and is_garden_saved:
		GardenUserRelationship.objects.get(userprofile=request.user.userprofile, garden=garden).delete()

	return HttpResponse("Success!")
