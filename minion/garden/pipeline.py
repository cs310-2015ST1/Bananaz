from garden.models import UserProfile


def save_profile(response, user, *args, **kwargs):
    my_user = UserProfile.objects.get_or_create(user=user)[0]
    my_user.photo = response['profile_image_url']
    my_user.oauth_token = response['access_token']['oauth_token']
    my_user.oauth_token_secret = response['access_token']['oauth_token_secret']
    my_user.save()
