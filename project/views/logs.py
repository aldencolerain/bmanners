from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from project.models import *
import logging
logger = logging.getLogger(__name__)


@user_passes_test(lambda u: u.is_superuser)
def index(request):
	context = {}
	context['entries'] = Entry.objects.order_by("-id").all()[:1000]
	return render(request, 'logs/index.html', context)

@csrf_exempt
def api_create(request):
	if request.POST.get('secret') != settings.API_SECRET:
	 	return HttpResponse('Unauthorized', status=401)
	server_ip = request.POST['ip']
	server_name = request.POST['name']
	message = request.POST['line']
	Entry(server_ip=server_ip, server_name=server_name, message=message).save()
	return HttpResponse("Success")