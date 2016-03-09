from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from project.models import Reservation
from django.http import JsonResponse
from django.conf import settings
import logging
logger = logging.getLogger(__name__)


@login_required
def manage(request):
	context = {}
	context['reservation'] = Reservation.current()
	return render(request, 'reservations/manage.html', context)

@login_required
def create(request):
	if not Reservation.current():
		map = request.POST.get('map', 'city').lower()
		Reservation(profile=request.user.profile, map=map).save()
	return redirect('reservations.manage')

@login_required
def delete(request):
	current_reservation = Reservation.current()
	if current_reservation and current_reservation.profile == request.user.profile:
		current_reservation.delete()
	return redirect('reservations.manage')

@csrf_exempt
def api_show(request):
	if request.POST.get('secret') != settings.API_SECRET:
		return JsonResponse({'error':'Unauthorized'}, status=401)
	reservation = Reservation.current()
	if reservation:
		return JsonResponse({'password':reservation.password, 'map': reservation.map})
	else:
		return JsonResponse({'password':'keepoutpls', 'map':'city'})