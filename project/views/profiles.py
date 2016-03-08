from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from project.extensions.shortcuts import sensitive
from project.forms.profile_forms import *
import logging
logger = logging.getLogger(__name__)


@sensitive
def create(request):
	form = CreateProfileForm()
	return render(request, 'profiles/create.html', {'form': form})

@sensitive
def create_post(request):
	form = CreateProfileForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user = form.save(commit=False)
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('index')
	return render(request, 'profiles/create.html', {'form': form})

@sensitive
def edit(request):
	form = EditProfileForm(request.user)
	return render(request, 'profiles/edit.html', {'form': form})

@sensitive
def edit_post(request):
	form = EditProfileForm(request.user, data=request.POST)
	if form.is_valid():
		form.save()
		update_session_auth_hash(request, form.user)
		return redirect('profile')
	return render(request, 'profiles/edit.html', {'form': form})