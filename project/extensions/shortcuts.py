from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

def sensitive(func):
	return sensitive_post_parameters()(csrf_protect(never_cache(func)))