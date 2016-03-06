from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^logs$', LogView.as_view(), name='logs'),
	url(r'^admin/', include(admin.site.urls)),
]