import ftplib
import csv
from django.http import HttpResponse
import re
from garden.models import Garden, FoodTree

# File located at ftp://webftp.vancouver.ca/OpenData/csv/CommunityGardensandFoodTrees.csv
IMPORT_SERVER = "webftp.vancouver.ca"
IMPORT_LOCATION = "OpenData/csv/CommunityGardensandFoodTrees.csv"
STORAGE_LOCATION = "data/CommunityGardensandFoodTrees.csv"


def import_garden_data(request):
    """Function that kicks off our importing"""
    csvfile = download_ftp_file()
    flush_gardens_and_trees()
    parse_downloaded_file(csvfile)
    return HttpResponse("Success!")


def download_ftp_file():
    """Retrieve Garden data csv file and store in root directory"""
    ftp = ftplib.FTP(IMPORT_SERVER)
    ftp.login()

    # Download file and overwrite existing
    ftp.retrbinary("RETR %s" % IMPORT_LOCATION, open(STORAGE_LOCATION, "wb").write)
    ftp.close()
    return open(STORAGE_LOCATION)


def flush_gardens_and_trees():
    """Clear old data"""
    Garden.objects.all().delete()


def parse_downloaded_file(csvfile):
    reader = csv.DictReader(csvfile)
    food_list = generate_food_list()
    for row in reader:
        if is_valid_garden(row):
            garden = Garden.objects.create(
                name=row["Name"],
                latitude=row["Latitude"],
                longitude=row["Longitude"]
            )
            parse_food_trees(row["FoodTreeVarieties"], garden, food_list)


def is_valid_garden(row):
    """Check that fields required for Garden model are present"""
    return row["Latitude"] and row["Longitude"] and row["Name"]


def parse_food_trees(food_trees, garden, food_list):
    """Finds foods that match given food list"""
    for tree_text in food_trees.lower().split(","):
        found_food = None
        for food in food_list:
            # if word(s) of food are found in the comma separated list of trees, then add it as a food tree
            if food in tree_text:
                if not found_food:
                    found_food = food
                else:
                    # Don't add food if we find multiple foods in one section
                    found_food = None
                    break

        if found_food:
            add_food_tree(tree_text, found_food, garden)


def add_food_tree(tree_text, food, garden):
    # from http://stackoverflow.com/questions/4289331/python-extract-numbers-from-a-string
    amounts = [int(s) for s in re.findall(r'\d+', tree_text)]
    try:
        amount = amounts[0]
    except IndexError:
        amount = 1

    existing_tree = garden.foodtree_set.filter(food_type__exact=food)

    if existing_tree:
        existing_tree[0].amount += amount
        existing_tree[0].save()
    else:
        FoodTree.objects.create(
            garden=garden,
            amount=amount,
            food_type=food
        )


# Modified from http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
def generate_food_list():
    """Convert line-separated food list to array of lowercase strings"""
    return [line.rstrip('\n').lower() for line in open("data/food_list.txt")]
