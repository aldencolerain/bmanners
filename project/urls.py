from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'project.views.home', name='home'),
	url(r'^admin/', include(admin.site.urls)),
]