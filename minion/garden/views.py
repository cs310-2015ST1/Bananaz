from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Garden
from .models import FoodTree

# Create your views here.
def index(request):
	food_types = generate_food_types()
	gardens = Garden.objects.order_by('name')
	return render(request,'garden/index.html',
			{'gardens' : gardens, 'food_types' : food_types})

def generate_food_types():
	food_types = []
	all_trees = FoodTree.objects.order_by('food_type')

	for item in all_trees:
		if not (item.food_type in food_types):
			food_types.append(item.food_type)

	return food_types

def search_criteria(request):

	gardens = Garden.objects.order_by('name')

	food_types = generate_food_types()
	treeobjects = FoodTree.objects.order_by('food_type')
	dict_of_mapping_from_garden_to_fruits = {}

	try:
		name_of_garden = request.POST['name']
		list_of_fruits = request.POST.getlist('fruit')
	except:
		return render(request, 'garden/search_criteria.html',
			{'gardens' : gardens, "trees" : food_types})

	if ((name_of_garden == '') and ((list_of_fruits.__len__() == 0) or ("all" in list_of_fruits))):
		return render(request, 'garden/search_criteria.html',
			{'gardens' : gardens, "trees" : food_types})

	elif (name_of_garden == ''):
		gardens = [];
		for tree in treeobjects:
			if tree.food_type in list_of_fruits:
				if tree.garden in gardens:
					pass
				else:
					gardens.append(tree.garden)

	elif (list_of_fruits.__len__() == 0):
		gardenstemp = Garden.objects.order_by('name')
		gardens = []
		for garden in gardenstemp:
			if (name_of_garden in garden.name):
				gardens.append(garden)

	else:
		if not ("all" in list_of_fruits):
			gardens = [];
			for tree in treeobjects:
				if tree.food_type in list_of_fruits:
					if tree.garden in gardens:
						pass
					else:
						gardens.append(tree.garden)
		gardenstemp = gardens[:]
		gardens = []
		for garden in gardenstemp:
			if (name_of_garden in garden.name):
				gardens.append(garden)

	return render(request, 'garden/index.html',
			{'gardens' : gardens, "food_types" : food_types})