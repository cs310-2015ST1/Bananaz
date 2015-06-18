# import StringIO
# from decimal import Decimal
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from garden.models import Garden, FoodTree
# from minion import ajax_import
# from django.http import HttpRequest, QueryDict, HttpResponse
# from minion.garden.views import search_criteria
# # from minion.minion.ajax_import import import_garden_data
#
#
# def create_garden(name='Garden', latitude=0, longitude=0):
#     return Garden.objects.create(
#         name=name,
#         latitude=latitude,
#         longitude=longitude,
#     )
#
#
# def create_food_tree(garden, amount=1, food_type='apple'):
#     return FoodTree.objects.create(
#         garden=garden,
#         amount=amount,
#         food_type=food_type,
#     )
#
#
# def make_ajax_request(self_object, mock_file_download_location):
#     ajax_import.download_ftp_file = lambda: open(mock_file_download_location)
#     return self_object.client.post(reverse("ajax_import"))
#
#
# def create_dict_line(name="Garden", latitude="0", longitude="0", food_tree_varieties=""):
#     return name + "," + latitude + "," + longitude + "," + food_tree_varieties + "\n"
#
#
# def create_http_request_object(name, list_of_foods):
#     object = HttpRequest()
#     dict = {'name': name, 'foods': list_of_foods}
#     qdict = QueryDict('', mutable=True)
#     qdict.update(dict)
#     object.GET = qdict
#     return object
#
#
#
#
# class AjaxImportTests(TestCase):
#     def test_ajax_import_with_one_garden(self):
#         response = make_ajax_request(self, "test/oneGarden.csv")
#         self.assertEqual("Success!", response.content)
#
#         self.assertEqual(Garden.objects.all().count(), 1)
#
#         g = Garden.objects.all()[0]
#         self.assertAlmostEqual(Decimal(10.5), g.latitude)
#         self.assertAlmostEqual(Decimal(3.3), g.longitude)
#         self.assertEqual("One", g.name)
#
#     def test_ajax_import_with_one_garden_one_tree(self):
#         response = make_ajax_request(self, "test/oneGardenOneTree.csv")
#         self.assertEqual("Success!", response.content)
#
#         self.assertEqual(Garden.objects.all().count(), 1)
#         self.assertEqual(FoodTree.objects.all().count(), 1)
#
#         f = FoodTree.objects.all()[0]
#         self.assertEqual(1, f.amount)
#         self.assertEqual(Garden.objects.all()[0], f.garden)
#         self.assertEqual("apple", f.food_type)
#
#     def test_ajax_import_with_duplicate_food_type(self):
#         response = make_ajax_request(self, "test/duplicateFoodType.csv")
#         self.assertEqual("Success!", response.content)
#
#         f = FoodTree.objects.all()[0]
#         self.assertEqual(4, f.amount)
#
#     def test_ajax_import_with_invalid_food_types(self):
#         response = make_ajax_request(self, "test/invalidFoodTypes.csv")
#         self.assertEqual("Success!", response.content)
#
#         self.assertEqual(Garden.objects.all().count(), 1)
#         self.assertEqual(FoodTree.objects.all().count(), 0)
#
#     def test_ajax_import_with_multiple_gardens_and_trees(self):
#         response = make_ajax_request(self, "test/multipleGardensAndTrees.csv")
#         self.assertEqual("Success!", response.content)
#
#         self.assertEqual(Garden.objects.all().count(), 2)
#         self.assertEqual(FoodTree.objects.all().count(), 4)
#
#         g = Garden.objects.filter(name="One")[0]
#         self.assertAlmostEqual(Decimal(10.5), g.latitude)
#         self.assertAlmostEqual(Decimal(3.3), g.longitude)
#         self.assertEqual(1, g.foodtree_set.count())
#         self.assertEqual(2, g.foodtree_set.filter(food_type="apple")[0].amount)
#
#         g = Garden.objects.filter(name="Two")[0]
#         self.assertAlmostEqual(Decimal(55.5), g.latitude)
#         self.assertAlmostEqual(Decimal(22.2), g.longitude)
#         self.assertEqual(3, g.foodtree_set.count())
#         self.assertEqual(1, g.foodtree_set.filter(food_type="apricot")[0].amount)
#         self.assertEqual(3, g.foodtree_set.filter(food_type="blueberry")[0].amount)
#         self.assertEqual(5, g.foodtree_set.filter(food_type="blackberry")[0].amount)
#
#
#
# class FlushGardenTests(TestCase):
#     def test_flush_garden_and_trees_with_one_garden(self):
#         g = create_garden()
#
#         self.assertEqual(Garden.objects.all().count(), 1)
#         self.assertEqual(FoodTree.objects.all().count(), 0)
#
#         ajax_import.flush_gardens_and_trees()
#
#         self.assertEqual(Garden.objects.all().count(), 0)
#         self.assertEqual(FoodTree.objects.all().count(), 0)
#
#     def test_flush_garden_and_trees_with_one_garden_and_tree(self):
#         g = create_garden()
#         create_food_tree(g)
#
#         self.assertEqual(Garden.objects.all().count(), 1)
#         self.assertEqual(FoodTree.objects.all().count(), 1)
#
#         ajax_import.flush_gardens_and_trees()
#
#         self.assertEqual(Garden.objects.all().count(), 0)
#         self.assertEqual(FoodTree.objects.all().count(), 0)
#
#     def test_flush_garden_and_trees_with_many_gardens_and_trees(self):
#         create_garden()
#
#         g = create_garden()
#         create_food_tree(g)
#
#         g = create_garden()
#         create_food_tree(g)
#         create_food_tree(g)
#         create_food_tree(g)
#
#         self.assertEqual(Garden.objects.all().count(), 3)
#         self.assertEqual(FoodTree.objects.all().count(), 4)
#
#         ajax_import.flush_gardens_and_trees()
#
#         self.assertEqual(Garden.objects.all().count(), 0)
#         self.assertEqual(FoodTree.objects.all().count(), 0)
#
#
#
# class SearchCriteriaTests(TestCase):
#     def test_search_for_a_garden_with_name_success(self):
#         response = make_ajax_request(self, "test/oneGardenOneTree.csv")
#         g = Garden.objects.all()
#
#         name = 'One'
#         list_of_foods = []
#         request = create_http_request_object(name, list_of_foods)
#         httpresponse = search_criteria(request)
#         got = httpresponse.context['name']
#         self.assertEqual(got, 'One')
#
#         # response = HttpResponse()
