from django import forms

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
