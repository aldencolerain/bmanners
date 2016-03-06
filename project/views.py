from django.shortcuts import render
from django.views.generic import View
from models import *
from django.conf import settings
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

class LogView(View):
	def post(self, request):
		if request.POST.get('secret') != settings.API_SECRET:
		 	return HttpResponse('Unauthorized', status=401)
		server_ip = request.POST['ip']
		server_name = request.POST['name']
		message = request.POST['line']
		Entry(server_ip=server_ip, server_name=server_name, message=message).save()
		return HttpResponse("Success")

	def get(self, request):
		context = {}
		context['entries'] = Entry.objects.all()
		return render(request, 'logs.html', context)


def home(request):
	context = {}
	return render(request, 'index.html', context)