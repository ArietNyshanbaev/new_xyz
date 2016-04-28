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

	def clean_username(self):
		cd = self.cleaned_data
		if User.objects.filter(username=cd['username']).exists():
			raise forms.ValidationError('Этот логин уже зарегистрирован')
		return cd['username']
	def clean_email(self):
		cd = self.cleaned_data
		if User.objects.filter(email=cd['email']).exists():
			raise forms.ValidationError('Этот email уже используется')
		return cd['email']

class InstanceModifyForm(forms.Form):
	CONDITION2 = (
    ('Новый (как новый)', 'Новый (как новый)'),
    ('Отличный (есть небольшие царапины )', 'Отличный (есть небольшие царапины )'),
    ('Среднее(есть царапины и потертости)', 'Среднее(есть царапины и потертости)'),
    ('Плохое (есть сколы, треск, разбитый экран и т.д.)', 'Плохое (есть сколы, треск, разбитый экран и т.д.)'),
    ('На запчасти', 'На запчасти'),
)
	CONDITION = (('Ariet', 'Aidai'), ('Aidai', 'Ariet'))
	CONDITION3 = ('Ariet', 'Aidai')
	title = forms.CharField(
		label=' Название объявления ',
		required=True,
		max_length=100,
		widget=forms.TextInput(attrs={'required': 'true'})
	)

	condition = forms.ChoiceField(
		label=' Название объявления2 ',
		required=True,
        choices=CONDITION
    )
