from django.shortcuts import render
from models import *

def home(request):
	context = {}
	return render(request, 'index.html', context)

def logs(request):
	context = {}
	return render(request, 'logs.html', context)