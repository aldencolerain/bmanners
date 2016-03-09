from pdb import set_trace as debugger
from django import template
from django.template.base import Node
from django.utils.html import format_html
from django.template import TemplateSyntaxError
from django.core.exceptions import ImproperlyConfigured, ViewDoesNotExist
from django.utils import six
from django.utils.encoding import force_str
from django.core.urlresolvers import (RegexURLPattern, RegexURLResolver, LocaleRegexURLResolver, ResolverMatch, LocaleRegexProvider)
from django.db import models
from django.http import JsonResponse
import json
from threading import current_thread
from functools import wraps
from django.http.response import HttpResponseRedirect


#
# middleware
#
class RestMiddleware(object):

	def process_request(self, request):
		# add parsed json data to request
		request.json = None
		if 'application/json' in request.META.get('CONTENT_TYPE', []):
			try: request.json = json.loads(request.body)
			except: pass		
		# attach method label or http method override label for rest routing
		method = request.POST.get('methodoverride', request.method).upper()
		current_thread().the_rest_request_method = method

	def process_exception(self, request, exception):
		# process json exceptions and unexpected exceptions
		if isinstance(exception, JsonException):
			return JsonResponse(exception.data, status=exception.status_code)


#
# custom json exception
#
class JsonException(Exception):
	def __init__(self, message, status_code):
		self.status_code = status_code
		if not isinstance(message, dict):
			self.data = {'error': str(message)}
		else:
			self.data = message
		super(JsonException, self).__init__(str(message))


#
# custom login required decorator
#
def json_login_required(func):
	@wraps(func)
	def wrapper(request, *args, **kwargs):
		if request.user.is_authenticated():
			return func(request, *args, **kwargs)
		raise JsonException('You must be authenticated to access this resource', 401)
	return wrapper


#
# custom url routers for restful routes
#


# decorator allows json routes to return a dictionary that will be automatically convert to json response
from functools import wraps
def json_response(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		response = func(*args, **kwargs)
		if isinstance(response, dict):
			return JsonResponse(response)
		elif hasattr(response, '__iter__'):
			return JsonResponse({m.id:m.to_dict() for m in response})
		elif hasattr(response, 'to_dict'):
			return JsonResponse(response.to_dict())
		return response
	return wrapper

# custom URL pattern for rest urls that checks the request method or method override
class RestURLPattern(RegexURLPattern):
	def __init__(self, regex, method, callback, default_args=None, name=None):
		self.method = method.upper()
		super(RestURLPattern, self).__init__(regex, callback, default_args=default_args, name=name)

	def resolve(self, path):
		if hasattr(current_thread(), 'the_rest_request_method'):
			request_method = current_thread().the_rest_request_method
			if request_method != self.method: return None
		return super(RestURLPattern, self).resolve(path)

# json rest url router
def json_url(regex, method, view, kwargs=None, type='html', name=None, prefix=''):
	view.json_view = True
	view = json_response(view)
	return rest_url(regex, method, view, kwargs=kwargs, name=name, prefix=prefix)

# rest url router (code is taken from django's url function)
def rest_url(regex, method, view, kwargs=None, name=None, prefix=''):	
	if isinstance(view, (list, tuple)):
		urlconf_module, app_name, namespace = view
		return RegexURLResolver(regex, urlconf_module, kwargs, app_name=app_name, namespace=namespace)
	elif callable(view):
		if prefix: view = prefix + '.' + view
		return RestURLPattern(regex, method, view, kwargs, name)
	else:
		raise TypeError('view must be a callable or a list/tuple in the case of include().')


#
# custom tag for http form method overwrite
#

# create library and add to built in tags
register = template.Library()

# method override tag
class MethodOverrideNode(Node):
	def __init__(self, method):
		self.method = method

	def render(self, context):
		method = self.method.resolve(context, True).upper()
		if method not in ['GET', 'POST', 'PUT', 'DELETE']:
			raise TemplateSyntaxError("The method tag argument must be GET PUT POST or DELETE.")
		return format_html("<input type='hidden' name='methodoverride' value='{}' />", method)

@register.tag('method')
def method_tag(parser, token):
	tokens = token.split_contents()
	if len(tokens) < 2:
		raise TemplateSyntaxError("The method tag requires at least 2 arguments.")
	return MethodOverrideNode(parser.compile_filter(tokens[1]))