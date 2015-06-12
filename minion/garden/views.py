from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Garden
from .models import FoodTree

# Create your views here.
def index(request):

    gardens = Garden.objects.order_by('name')

    trees = []
    treeobjects = FoodTree.objects.order_by('food_type')
    dict_of_mapping_from_garden_to_fruits = {}

    for item in treeobjects:
        if not (item.food_type in trees):
            trees.append(item.food_type)

    # if True:
    #     return render(request,'garden/index.html',{'gardens' : gardens, "trees" : trees})
    if not (('fruit' in request.GET) and ('name' in request.GET)):
        return render(request,'garden/index.html', {'gardens' : gardens, "trees" : trees})
    else:
        name_of_garden = request.GET['name']
        list_of_fruits = request.GET.getlist('fruit')

    # except (UnicodeDecodeError, MultiValueDictKeyError):
    #     return render(request,'garden/index.html',
    #         {'gardens' : gardens, "trees" : trees})

    if ((name_of_garden == '') and ((list_of_fruits.__len__() == 0) or ("all" in list_of_fruits))):
        return render(request,'garden/index.html',
            {'gardens' : gardens, "trees" : trees})

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

    return render(request,'garden/index.html',
            {'gardens' : gardens, "trees" : trees})



# def search_criteria(request):
#
# 	gardens = Garden.objects.order_by('name')
#
# 	trees = []
# 	treeobjects = FoodTree.objects.order_by('food_type')
# 	dict_of_mapping_from_garden_to_fruits = {}
#
# 	for item in treeobjects:
# 		if not (item.food_type in trees):
# 			trees.append(item.food_type)
#
# 	try:
# 		name_of_garden = request.GET['name']
# 		list_of_fruits = request.GET.getlist('fruit')
# 	except:
# 		return render(request,'search_criteria.html',
# 			{'gardens' : gardens, "trees" : trees})
#
# 	if ((name_of_garden == '') and ((list_of_fruits.__len__() == 0) or ("all" in list_of_fruits))):
# 		return render(request,'search_criteria.html',
# 			{'gardens' : gardens, "trees" : trees})
#
# 	elif (name_of_garden == ''):
# 		gardens = [];
# 		for tree in treeobjects:
# 			if tree.food_type in list_of_fruits:
# 				if tree.garden in gardens:
# 					pass
# 				else:
# 					gardens.append(tree.garden)
#
# 	elif (list_of_fruits.__len__() == 0):
# 		gardenstemp = Garden.objects.order_by('name')
# 		gardens = []
# 		for garden in gardenstemp:
# 			if (name_of_garden in garden.name):
# 				gardens.append(garden)
#
# 	else:
# 		if not ("all" in list_of_fruits):
# 			gardens = [];
# 			for tree in treeobjects:
# 				if tree.food_type in list_of_fruits:
# 					if tree.garden in gardens:
# 						pass
# 					else:
# 						gardens.append(tree.garden)
# 		gardenstemp = gardens[:]
# 		gardens = []
# 		for garden in gardenstemp:
# 			if (name_of_garden in garden.name):
# 				gardens.append(garden)
#
# 	return render(request,'search_criteria.html',
# 			{'gardens' : gardens, "trees" : trees})