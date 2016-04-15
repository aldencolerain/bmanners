from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from project.extensions.bmservers import get_servers, get_latest_version
import logging
logger = logging.getLogger(__name__)


@cache_page(30)
def index(request):
	bm_version = cache.get('bm_version')
	if bm_version:
		bm_version = get_latest_version()
		cache.set('bm_version', bm_version, 60)
	servers = get_servers(version=bm_version)
	return render(request, 'servers/index.html', {'servers': servers})