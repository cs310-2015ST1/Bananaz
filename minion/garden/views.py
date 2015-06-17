from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth import logout as auth_logout
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from Account import UserProfile


from .models import Garden
from .models import FoodTree

def index(request):
	food_types = generate_food_types()
	gardens = Garden.objects.order_by('name')
	return render_index(request, gardens, food_types)


# twitterauth
def login(request):
	# return render(request, 'login.html')
	return render_to_response("Account/login.html", {"user":request.user})


#@login_required(login_url='/')
def home(request):
#	return render_to_response('home.html', context)
	return render_to_response("Account/home.html", {"user" : request.user})


def logout(request):
    auth_logout(request)
  #  return redirect('/')
  return HttpResponseRedirect("/login")


def render_index(request, gardens, food_types):
	return render(request, 'garden/index.html',
				{'gardens': gardens, 'food_types': food_types})


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
		list_of_foods = request.POST.getlist('foods')
	except MultiValueDictKeyError:
		return render_index(request, all_gardens, food_types)

	# empty search
	if ignore_name(name_of_garden) and ignore_foods(list_of_foods):
		return render_index(request, all_gardens, food_types)

	elif ignore_name(name_of_garden):
		gardens = filter_by_foods(all_food_trees, list_of_foods)

	elif ignore_foods(list_of_foods):
		gardens = filter_by_name(all_gardens, name_of_garden)

	else:
		gardens = filter_by_foods(all_food_trees, list_of_foods)
		gardens = filter_by_name(gardens, name_of_garden)

	return render_index(request, gardens, food_types)


def filter_by_name(gardens, name_of_garden):
	filtered_gardens = []
	for garden in gardens:
		if name_of_garden in garden.name:
			filtered_gardens.append(garden)
	return filtered_gardens


def filter_by_foods(all_food_trees, list_of_foods):
	gardens = []
	for tree in all_food_trees:
		if tree.food_type in list_of_foods:
			if tree.garden in gardens:
				pass
			else:
				gardens.append(tree.garden)
	return gardens


def ignore_name(name_of_garden):
	return name_of_garden == ''


def ignore_foods(list_of_foods):
	return (list_of_foods.__len__() == 0) or ("all" in list_of_foods)


#twitterprofile



# def get_user_avatar(backend, details, response, social_user, uid,
#                     user, *args, **kwargs):
#     url = None
#     if backend.__class__ == FacebookBackend:
#         url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

#     elif backend.__class__ == TwitterBackend:
#         url = response.get('profile_image_url', '').replace('_normal', '')

#     if url:
#         profile = user.get_profile()
#         avatar = urlopen(url).read()
#         fout = open(filepath, "wb") #filepath is where to save the image
#         fout.write(avatar)
#         fout.close()
#         profile.photo = url_to_image # depends on where you saved it
#         profile.save()