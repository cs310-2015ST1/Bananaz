from django.contrib.auth.models import User
from garden.models import UserProfile
from social.backends.twitter import TwitterOAuth


def save_profile(backend, details, response, social_user, uid,
                    user, *args, **kwargs):
    url = None
 # backend.__class__ == TwitterOAuth:
    url = response.get['profile_image_url']

    if url:
        profile = user.get_profile()
        avatar = urlopen(url).read()
        fout = open(filepath, "wb") #filepath is where to save the image
        fout.write(avatar)
        fout.close()
        profile.photo = url_to_image # depends on where you saved it
        profile.save()



# def save_profile(backend, user, response, *args, **kwargs):
#     if backend.name == 'twitter':
#         profile = user.profile
#         if profile is None:
#             profile = Profile(user_id=user.id)
#         profile.gender = response.get('gender')
#         profile.link = response.get('link')
#         profile.timezone = response.get('timezone')
#         profile.save()



# def get_profile_picture(
# 	strategy,
# 	user,
# 	response,
# 	details,
# 	is_new = False,
# 	*args,
# 	**kwards):
# 	img_url = None

# 	if backend.name == 'twitter':
# 		img_url = "http://graph.facebook.com/%s/"

# 	#profile = UserProfile.objects.get_or_create(user = user)[0]

# 	# if backend.name == 'twitter':
# 	# 	if response['profile_image_url'] != '':
# 	# 		if not response.get('default_profile_image'):
# 	# 			avatar_url = response.get('profile_image_url_https')
# 	# 			if avatar_url:
# 	# 				avatar_url = avatar_url.replace('_normal.', '_bigger.')
# 	# 				img_url = avatar_url
# 		# img_url = response.get('profile_image_url', '').replace('_normal', '')

# 	profile.photo = img_url
# 	profile.save()