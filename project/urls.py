from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^logs$', csrf_exempt(LogView.as_view()), name='logs'),
	url(r'^admin/', include(admin.site.urls)),
]