from django.contrib.auth.models import User
from garden.models import UserProfile
from social.backends.twitter import TwitterOAuth


def fetch_or_create_user(user):
    try:
        my_user = user.userprofile
    except Exception:
        my_user = UserProfile.objects.create(
            user=user
        )
    return my_user


def update_user_data(my_user, response):
    my_user.photo = response['profile_image_url']
    my_user.save()


def save_profile(backend, details, response, uid,
                    user, *args, **kwargs):
    my_user = fetch_or_create_user(user)
    update_user_data(my_user, response)



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