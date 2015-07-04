from django.conf.urls import url
from . import views
from minion import minion

urlpatterns = [
	url(r'^$', views.index, name='index'),

	# twitterauth
	url(r'^logout/$', views.logout, name='logout'),

	url(r'^search_criteria/$', views.search_criteria, name='search_criteria'),

	url(r'^updateusers/$', minion.minion.ajax_update_users.import_user_data, name='ajax_update_users'),

]
