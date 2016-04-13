from django.http import JsonResponse
from django.shortcuts import render, redirect
from project.models import Tournament
import logging
logger = logging.getLogger(__name__)


def show(request):
	tournament = Tournament.get()
	return render(request, 'tournaments/show.html', {'tournament':tournament})

def edit(request):
	tournament = Tournament.get()
	try:
		number = int(request.POST['number'])
		tournament.matches[number]['top_player'] = request.POST.get('top_player')
		tournament.matches[number]['bottom_player'] = request.POST.get('bottom_player')
		tournament.matches[number]['top_score'] = request.POST.get('top_score')
		if tournament.matches[number]['top_score']:
			tournament.matches[number]['top_score'] = int(tournament.matches[number]['top_score'])
		tournament.matches[number]['bottom_score'] = request.POST.get('bottom_score')
		if tournament.matches[number]['bottom_score']:
			tournament.matches[number]['bottom_score'] = int(tournament.matches[number]['bottom_score'])
		tournament.save()
	except ValueError:
		pass

	return redirect('tournaments.show')

def api_show(request):
	if request.POST.get('secret') != settings.API_SECRET:
		return JsonResponse({'error':'Unauthorized'}, status=401)
	reservation = Reservation.current()
	if reservation:
		return JsonResponse({'password':reservation.password, 'map': reservation.map})
	else:
		return JsonResponse({'password':'keepoutpls', 'map':'city'})
