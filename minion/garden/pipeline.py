from garden.models import UserProfile

def get_profile_picture(
	strategy,
	user,
	response,
	details,
	is_new = False,
	*args,
	**kwards):
	img_url = None

	profile = UserProfile.objects.get_or_create(user = user)[0]

	if backend.name == 'twitter':
		if response['profile_image_url'] != '':
			if not response.get('default_profile_image'):
				avatar_url = response.get('profile_image_url_https')
				if avatar_url:
					avatar_url = avatar_url.replace('_normal.', '_bigger.')
					img_url = avatar_url
		# img_url = response.get('profile_image_url', '').replace('_normal', '')

	profile.photo = img_url
	profile.save()