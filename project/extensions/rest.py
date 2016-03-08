from django.http import HttpResponseNotAllowed
import logging
logger = logging.getLogger(__name__)


http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

def build_http_method_not_allowed(allowed_methods):
	def http_method_not_allowed(request, *args, **kwargs):
		logger.warning('Method Not Allowed (%s): %s', request.method, request.path,
			extra={
				'status_code': 405,
				'request': request
			}
		)
		return HttpResponseNotAllowed(allowed_methods)
	return http_method_not_allowed
		
def rest(**views):
	def dispatch(request, *args, **kwargs):
		if request.method.lower() in http_method_names:
			handler = views.get(request.method.lower(), build_http_method_not_allowed(views.keys()))
		else:
			handler = build_http_method_not_allowed(views.keys())
		return handler(request, *args, **kwargs)
	return dispatch