from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import views, authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__)


def signin(request):
	return views.login(request, template_name='auth/signin.html')

def signout(request):
	return views.logout(request, next_page='index')

def reset(request):
	#from_email/subject_template_name/email_template_name
	return views.password_reset(request, template_name='auth/reset.html', post_reset_redirect='reset')

def reset_confirm(request, uidb64=None, token=None):
	return views.password_reset_confirm(request, uidb64, token, template_name='auth/reset_confirm.html', post_reset_redirect='signin')





