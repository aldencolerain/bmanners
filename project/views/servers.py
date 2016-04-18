from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from project.extensions.bmservers import get_servers, get_latest_version
import logging
logger = logging.getLogger(__name__)


def get_servers_cached():
	bm_version = cache.get('bm_version')
	if bm_version:
		bm_version = get_latest_version()
		cache.set('bm_version', bm_version, 60)
	servers = get_servers(version=bm_version)
	return servers

@cache_page(30)
def index(request):
	servers = get_servers_cached()
	return render(request, 'servers/index.html', {'servers': servers})

@cache_page(30)
def api_show(request, name):
	servers = get_servers_cached()
	matching_servers =  [s for s in servers if name in s.get('name', '')]
	return JsonResponse({'servers': matching_servers})
