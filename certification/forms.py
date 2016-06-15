from django import forms 

class OrderForm(forms.Form):
	
	number = forms.CharField(
		label=' Номер телефона ', 
		required=True, 
		max_length=45,
		widget=forms.TextInput(attrs={'required': 'true'})
	)
	email = forms.CharField(
		label=' Email',
		max_length=100,
		widget=forms.EmailInput()
	)
	note = forms.CharField(
		label=' Коментарии ',
		max_length=500,
		widget=forms.Textarea(attrs={'placeholder': 'например: Хочу узнать где можно забрать или Хочу купить завтра.'})
	)
