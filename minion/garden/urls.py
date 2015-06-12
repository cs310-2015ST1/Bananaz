from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),

		#twitterauth; MAY HAVE TO BE IN THE OTHER URLS.PY 
		url(r'^$', 'django_social_app.views.login'),
    	url(r'^home/$', 'django_social_app.views.home'),
    	url(r'^logout/$', 'django_social_app.views.logout'),
	]
