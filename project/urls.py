from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from extensions.rest import rest
from views import home
from views import auth
from views import logs
from views import profiles


urlpatterns = [
	url(r'^$', rest(get=home.index), name='index'),
	url(r'^reserve$', login_required(rest(get=home.reserve, post=home.reserve_post)), name='reserve'),
	url(r'^reserve/delete$', home.delete_reservation, name='delete_reservation'),
	url(r'^password$', csrf_exempt(rest(post=home.password)), name='password'),

	url(r'^signin$', auth.signin, name='signin'),
	url(r'^signout$', auth.signout, name='signout'),
	url(r'^reset$', auth.reset, name='reset'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$', auth.reset_confirm, name='password_reset_confirm'),

	url(r'^signup$', rest(get=profiles.create, post=profiles.create_post), name='signup'),
	url(r'^profile$', login_required(rest(get=profiles.edit, post=profiles.edit_post)), name='profile'),

	url(r'^logs$', rest(get=login_required(logs.logs), post=logs.logs_create), name='logs'),

	url(r'^admin/', include(admin.site.urls)),
]