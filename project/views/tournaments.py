from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)


def show(request):
	return render(request, 'tournaments/show.html', {})
