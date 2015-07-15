from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),

	# twitterauth
	url(r'^logout/$', views.logout, name='logout'),

	url(r'^search_criteria/$', views.search_criteria, name='search_criteria'),
	url(r'^tweet/$',views.get_tweet, name='tweet'),
	url(r'^form/',views.get_tweet, name='form'),
	url(r'^search_criteria/form/',views.get_tweet, name='form'),
	url(r'^save_garden/$', views.save_garden, name='save_garden'),

]
