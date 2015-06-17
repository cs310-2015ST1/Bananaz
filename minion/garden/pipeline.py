from garden.models import UserProfile

def get_profile_picture(
	user,
	response,
	details,
	is_new = False,
	*args,
	**kwards):
	img_url = None

	img_url = response.get('profile_image_url', '').replace('_normal', '')

	profile = UserProfile.objects.get_or_creat(user = user)[0]
	profile.photo = img_url
	profile.save()