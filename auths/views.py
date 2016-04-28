# pythone packages imports
from __future__ import unicode_literals
import re
# django core packages imports 
from django.shortcuts import redirect, get_object_or_404, render
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse , reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
#impoer of models
from .models import Information
from fishkas.models import Slogan, Wish, Notifier
from main.models import Category, Instance, Sold, Instance_buy, Device
# import of custom writen decorator and views
from custom_code.decorators import email_required, logout_required
from custom_code.ibox_views import need_for_every
from .forms import SigninForm, SignupForm, InstanceModifyForm

@logout_required
def signin(request, key='main'):
	# initialize variables
	args={}
	args.update(csrf(request))
	
	# retriving values from GET request
	test_next = request.GET.get('next', '')
	# adding message if needed
	if test_next and test_next != '/bet/make_bet':
		messages.add_message(request, messages.SUCCESS, 'Чтобы совершить данное действие вам нужно авторизоваться. ', fail_silently=True)
	need_for_every(args,request)

	if request.POST:
		form = SigninForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			username = cd['username']
			password = cd['password']

			user = authenticate(username=username, password=password)

			if user is None and User.objects.filter(email=username).exists():
				user = authenticate(username=User.objects.filter(email=username)[0].username, password=password)
			
			if user is not None:
				if user.is_active:
					login(request, user)
					# check if we got next value
					next_link = request.POST.get('next', '')
					if next_link != '' :
						return redirect(next_link)
					return redirect(reverse('main:main'))
				else:
					args['error_message'] = "Ваш аккаунт временно заблокирован"
			else:
				args['error_message'] = "Имя пользователя и пароль не совпадают, попробуйте еще раз. "
	else:
		form = SigninForm()
	args['form'] = form
	return render(request, 'auths/signin.html', args)

@logout_required
def signup(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args,request)
	validation = True
	# Query objects from model
	

	if request.POST:
		form = SignupForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			first_name = cd['name']
			username = cd['username']
			email = cd['email']
			password = cd['password']

			user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
			user.save()
			# authenticate and login user
			user_login = authenticate(username=username, password=password)
			login(request, user_login)
			messages.add_message(request, messages.SUCCESS, 'Вы успешно зарегистрировались на сайте', fail_silently=True)
			
			return redirect(reverse('main:main'))

	else:
		form = SignupForm()
	args['form'] = form
	return render(request, 'auths/signup.html', args)

@login_required(login_url=reverse_lazy('main:main'))
def signout(request):
	logout(request)

	return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=reverse_lazy('auths:signin'))
def profile(request):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request)
	args['devices'] = Device.objects.filter(user=request.user)

	return render(request, 'auths/profile.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
def modify_myinstance(request):
	# initialize variables
	args = {}
	args.update(csrf(request))

	if request.POST:
		title = request.POST.get('title', '')
		price = request.POST.get('price', '')
		min_price = request.POST.get('min_price', '')
		max_price = request.POST.get('max_price', '')
		phone_num = request.POST.get('phone_num', '')
		note = request.POST.get('note', '')
		instance_id = request.POST.get('instance_id', '')
		condition =  request.POST.get('condition', '')
		guarantee = request.POST.get('guarantee', '')
		exchange = request.POST.get('exchange', '')
		bargain = request.POST.get('bargain', '')
		sell_or_buy = request.POST.get('sell_or_buy', '')
		
		if sell_or_buy == 'sell':
			instance = get_object_or_404(Instance, pk=instance_id)
		else:
			instance = get_object_or_404(Instance_buy, pk=instance_id)

		if instance.user == request.user and sell_or_buy == 'sell':
			instance.title = title
			instance.price = price
			instance.telephones = phone_num
			instance.note = note
			instance.condition = condition
			instance.guarantee = guarantee
			if exchange == '1':
				instance.exchange = True
			else:
				instance.exchange = False
			if bargain == '1':
				instance.bargain = True
			else:
				instance.bargain = False
			instance.save()
			messages.add_message(request, messages.SUCCESS, 'Вы успешно отредактировали это обявление.', fail_silently=True)
		else:
			if int(min_price) > int(max_price):
				max_price, min_price = min_price, max_price
			args['min_price'] = min_price
			args['max_price'] = max_price
			args['title'] = title
			args['phone_num'] = phone_num
			args['note'] = note
			status = instance.update_info(args)
			messages.add_message(request, messages.SUCCESS, status, fail_silently=True)
	
	return redirect(reverse('auths:myinstances'))

@login_required(login_url=reverse_lazy('auths:signin'))
def delete_myinstance(request, instance_id, ads='sell'):
	# initialize variables
	args = {}
	args.update(csrf(request))
	# Query objects from model
	if ads == 'sell':
		instance = get_object_or_404(Instance, pk=instance_id)
	elif ads == 'buy' :
		instance = get_object_or_404(Instance_buy, pk=instance_id)
	else:
		messages.add_message(request, messages.SUCCESS, 'Совершить данную операцию невозможно.', fail_silently=True)
		return redirect(request.META.get('HTTP_REFERER'))

	if instance.user == request.user:
		instance.delete()
		messages.add_message(request, messages.SUCCESS, 'Объявление успешно удалено.', fail_silently=True)
		if ads == 'sell':
			sold = request.GET.get('sold', '')
			if sold == '1':
				Sold.objects.create(seller=request.user, date_added=instance.added_date, price=instance.price, model=instance.model, sold_at_ibox=True)
			else:
				Sold.objects.create(seller=request.user, date_added=instance.added_date, price=instance.price, model=instance.model, sold_at_ibox=False)
	return redirect(reverse('auths:myinstances'))

@login_required(login_url=reverse_lazy('auths:signin'))
def myinstances(request):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request)
	# Query objects from model
	instances = Instance.objects.filter(user=request.user).order_by('-added_date')
	instances_to_buy = Instance_buy.objects.filter(user=request.user).order_by('-added_date')
	# Passing arguments
	args['instances'] = instances
	args['instances_to_buy'] = instances_to_buy

	return render(request, 'auths/myinstances.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
def my_notify(request):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request)
	# Passing arguments
	args['notifiers'] = Notifier.objects.filter(user=request.user)

	return render(request, 'auths/my_notify.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
def my_wishlist(request):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args,request)
	# Query objects from model and assigning to context
	args['instances'] = Wish.objects.filter(user=request.user, for_buy=False).reverse()
	args['instances_to_buy'] = Wish.objects.filter(user=request.user, for_buy=True).reverse()

	return render(request, 'auths/mywishlist.html', args)


@login_required(login_url=reverse_lazy('auths:signin'))
def modify_profile(request):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args,request)
	validation = True
	user = request.user

	if request.POST:
		first_name = request.POST.get('first_name', '')
		email = request.POST.get('e_mail', '')

		# first_name validation
		if len(first_name) < 4 :
			args['first_name_error'] = 'Слишком короткое Ф.И.О'
			validation = False
		# email validation
		if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
			validation = False
			args['email_error'] = 'Неправильно введен email'
		else:
			# Query objects from model
			users_using_email = User.objects.all().filter(email=email)

			if users_using_email.count() > 0 and request.user.username[0:1] == users_using_email[0].username[0:1] and request.user.username != users_using_email[0].username:
				#args['email_error'] = 'Этот email уже используется'
				instances = Instance.objects.filter(user=users_using_email[0])
				if instances.count() > 0:
					for instance in instances:
						instance.user = request.user
						instance.save()
				wishes = Wish.objects.filter(user=users_using_email[0])
				if wishes.count() > 0:
					for wish in wishes:
						wish.user = request.user
						wish.save()
				user_to_change = get_object_or_404(User, email=email)
				user_to_change.email = ""
				user_to_change.save()
		if validation == False:
			# Passing arguments
			args['user'] = request.user

			return render(request, 'auths/modify_profile.html', args)

		user.email = email
		user.first_name = first_name
		user.save()
		messages.add_message(request, messages.SUCCESS, 'Ваш аккаунт успешно отредактирован.', fail_silently=True)
		args['user'] = request.user
		return redirect(reverse('auths:profile'))
	else:
		# Passing arguments
		args['user'] = user

		return render(request, 'auths/modify_profile.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
def change_password(request):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args,request)
	user = request.user

	if request.POST:
		password1 = request.POST.get('password1', '')
		password2 = request.POST.get('password2', '')
		# password validation
		if len(password1) < 6 or len(password2) < 6:
			args['password_error'] = 'Пароль должен состоять из 6 и более символов'
			return render(request, 'auths/change_password.html', args)
		if password1 == password2:
			user.set_password(password1)
			user.save()
			messages.add_message(request, messages.SUCCESS, 'Ваш пароль успешно изменен, войдите заново используя новый пароль.', fail_silently=True)
			return redirect(reverse('auths:signin'))
		else:
			args['password_error'] = 'Пароли не совпадают'
		return render(request, 'auths/change_password.html', args)
	else:
		return render(request, 'auths/change_password.html', args)

def profile_others(request, user_id):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request)
	# Query objects from model
	user_profile = get_object_or_404(User, pk=user_id)
	# Passing arguments
	args['user_profile'] = user_profile
	args['instances'] = Instance.objects.filter(user=user_profile).order_by('-added_date')
	args['instances_to_buy'] = Instance_buy.objects.filter(user=user_profile).order_by('-added_date')

	return render(request, 'auths/profile_others.html', args)
