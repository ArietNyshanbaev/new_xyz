from django import forms
# validation of user
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from .models import Verification

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
	email = forms.CharField(
		label=' Email',
		required=True,
		max_length=100,
		widget=forms.EmailInput(attrs={'required': 'true'})
	)

	password = forms.CharField(
		label=' Пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)

	def clean_username(self):
		cd = self.cleaned_data
		if User.objects.filter(username=cd['username']).exists():
			raise forms.ValidationError('Этот логин уже зарегистрирован')
		return cd['username']
	def clean_email(self):
		cd = self.cleaned_data
		temp_users = User.objects.filter(email=cd['email'])
		if temp_users.exists():
			verification = Verification.objects.filter(user=temp_users[0])
			if verification.exists():
				if verification[0].is_verified:
					raise forms.ValidationError('Этот email уже используется')
		return cd['email']

class InstanceModifyForm(forms.Form):
	CONDITION = (
    ('Новый (как новый)', 'Новый (как новый)'),
    ('Отличный (есть небольшие царапины )', 'Отличный (есть небольшие царапины )'),
    ('Среднее(есть царапины и потертости)', 'Среднее(есть царапины и потертости)'),
    ('Плохое (есть сколы, треск, разбитый экран и т.д.)', 'Плохое (есть сколы, треск, разбитый экран и т.д.)'),
    ('На запчасти', 'На запчасти'),
)
	title = forms.CharField(
		label=' Название объявления ',
		required=True,
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true'})
	)

	condition = forms.ChoiceField(
		label=' condition',
		required=True,
        choices=CONDITION
    )

class ChangePasswordForm(forms.Form):
	current_password = forms.CharField(
		label=' Нынешний пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)
	new_password = forms.CharField(
		label=' Новый пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)
	repeate_new_password = forms.CharField(
		label=' Повторите новый пароль ',
		required=True, 
		widget=forms.PasswordInput(attrs={'required': 'true'})
	)

	def clean_repeate_new_password(self):
		cd = self.cleaned_data
		if cd['repeate_new_password'] != cd['new_password'] :
			raise forms.ValidationError('Новые пароли не совпадают.')
		return cd['repeate_new_password']

class EnterEmailForm(forms.Form):
	email = forms.CharField(
		label=' Email ',
		required=True,
		max_length=100,
		widget=forms.EmailInput(attrs={'required': 'true'})
	)

	def clean_email(self):
		cd = self.cleaned_data
		user = User.objects.filter(email=cd['email'])
		if user.exists():
			verification = Verification.objects.filter(user=user[0])
			if verification.exists() and verification[0].is_verified == True:
				raise forms.ValidationError('Этот email уже используется.')
		return cd['email']
