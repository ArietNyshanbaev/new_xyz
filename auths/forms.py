from django import forms
# validation of user
from django.forms.util import ErrorList
from django.contrib.auth.models import User

class SigninForm(forms.Form):
	username = forms.CharField(
		label='Логин или email ', 
		required=True, 
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true'})
	)
	password = forms.CharField(
		label=' Пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)

class SignupForm(forms.Form):
	username = forms.CharField(
		label=' Логин ',
		required=True, 
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true'})
	)
	password = forms.CharField(
		label=' Пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)
	name = forms.CharField(
		label=' Фамилия и имя ',
		required=True, 
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true'})
	)
	email = forms.CharField(
		label=' Email (Скрыто от других пользователей)',
		required=True,
		max_length=100,
		widget=forms.EmailInput(attrs={'required': 'true'})
	)

	def is_unique_user(self):
		unique = True
		if User.objects.filter(username=self.cleaned_data['username']).exists():
			unique = False
			errors = self._errors.setdefault('username', ErrorList())
			errors.append(u"Этот логин уже зарегистрирован")
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			unique = False
			errors = self._errors.setdefault('email', ErrorList())
			errors.append(u"Этот email уже используется")
		return unique