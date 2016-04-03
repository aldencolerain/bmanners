from django.conf.urls import include, url
from django.contrib import admin
from extensions.rest import rest_url
from views import home
from views import auth
from views import logs
from views import profiles
from views import reservations
from views import tournaments


urlpatterns = [

	# home
	url(r'^$', home.index, name='home.index'),

	# auth
	url(r'^signin$', auth.signin, name='auth.signin'),
	url(r'^signout$', auth.signout, name='auth.signout'),
	url(r'^reset$', auth.reset, name='auth.reset'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', auth.reset_confirm, name='password_reset_confirm'),

	# tournament
	rest_url(r'^tournament$', 'GET', tournaments.show, name='tournaments.show'),

	# profiles
	rest_url(r'^signup$', 'GET', profiles.new, name='profiles.new'),
	rest_url(r'^signup$', 'POST', profiles.create, name='profiles.create'),
	rest_url(r'^profile$', 'GET', profiles.edit, name='profiles.edit'),
	rest_url(r'^profile$', 'PUT', profiles.update, name='profiles.update'),

	# reservations
	rest_url(r'^reservation$', 'GET', reservations.manage, name="reservations.manage"),
	rest_url(r'^reservation$', 'POST', reservations.create, name='reservations.create'),
	rest_url(r'^reservation$', 'DELETE', reservations.delete, name='reservations.delete'),

	# logs
	rest_url(r'^logs$', 'GET', logs.index, name='logs.index'),

	# api
	rest_url(r'^api/reservation$', 'POST', reservations.api_show, name='reservations.api_show'),
	rest_url(r'^api/logs$', 'POST', logs.api_create, name='logs.api_create'),

	# admin
	url(r'^admin/', include(admin.site.urls)),
]
