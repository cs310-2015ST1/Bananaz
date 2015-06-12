from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		#url(r'^search_criteria/$', views.search_criteria, name='search_criteria')

	]
