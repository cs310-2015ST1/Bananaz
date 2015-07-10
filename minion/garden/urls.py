from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),

	# twitterauth
	url(r'^logout/$', views.logout, name='logout'),

	url(r'^search_criteria/$', views.search_criteria, name='search_criteria'),
	url(r'^form/',views.get_tweet, name='form'),


]
