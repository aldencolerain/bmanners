from django.shortcuts import render, redirect
from project.models import Reservation
from django.http import JsonResponse
from django.conf import settings
import logging
logger = logging.getLogger(__name__)


def index(request):
	return render(request, 'index.html', {})

def reserve(request):
	context = {}
	context['reservation'] = Reservation.current()
	return render(request, 'reserve.html', context)

def reserve_post(request):
	if not Reservation.current():
		map = request.POST.get('map', 'city').lower()
		Reservation(profile=request.user.profile, map=map).save()
	return redirect('reserve')

def delete_reservation(request):
	current_reservation = Reservation.current()
	if current_reservation and current_reservation.profile == request.user.profile:
		current_reservation.delete()
	return redirect('reserve')

def password(request):
	if request.POST.get('secret') != settings.API_SECRET:
		return JsonResponse({'error':'Unauthorized'}, status=401)
	reservation = Reservation.current()
	if reservation:
		return JsonResponse({'password':reservation.password, 'map': reservation.map})
	else:
		return JsonResponse({'password':'keepoutpls', 'map':'city'})