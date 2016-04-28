from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

def email_required(f):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated() and not request.user.email :
			messages.add_message(request, messages.WARNING, 'Пожалуйста укажите ваш email чтобы продолжить.', fail_silently = True)
			return redirect(reverse('auths:modify_profile'))   
		return f(request, *args, **kwargs)
	wrap.__doc__=f.__doc__
	wrap.__name__=f.__name__
	return wrap

def logout_required(f):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated() :
			messages.add_message(request, messages.SUCCESS, 'Вы уже авторизовались .', fail_silently = True)
			return redirect(reverse('main:main')) 
		return f(request, *args, **kwargs)
	wrap.__doc__=f.__doc__
	wrap.__name__=f.__name__
	return wrap
