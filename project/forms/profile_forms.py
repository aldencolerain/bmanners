from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm as EditProfileForm

class CreateProfileForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "email")