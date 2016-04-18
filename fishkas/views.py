﻿# python package imports
import threading
# django core package imports
from django import template
from django.shortcuts import redirect, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.messages import get_messages
# import of custom writen decorator and views
from custom_code.decorators import email_required
from custom_code.ibox_views import need_for_every
#import of project models 
from .models import Wish, Message, Notifier, Slogan, Imei
from main.models import Category , Instance , Brand , Modell, City, Instance_buy

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def notify_me(request):
	# initialize variables
	args={}
	args.update(csrf(request))

	if request.POST:
		# retrieve values from form
		min_price = request.POST['from_price']
		max_price = request.POST['to_price']
		category_list = request.POST.getlist('category_name')
		
		category_list = list(category_list)
		# validation of prices
		if min_price == "" or int(min_price) < 1 or  max_price == "" or int(max_price) < 1:
			messages.add_message(request, messages.WARNING, 'Пожалуйста укажите суммы правильно.', fail_silently=True)
			return redirect(reverse('main:main'))
		if len(category_list) == 0:
			category_list = Category.objects.all()
			temporary = ""
			for category in category_list:
				temporary += category.title+","
		else:
			temporary = ""
			for category in category_list:
				temporary += category+","
		notify = Notifier.objects.create(user = request.user, min_price = min_price, max_price = max_price, categories=temporary[:-1])
		messages.add_message(request, messages.SUCCESS, 'Ваша напоминалка успешно создана.')
		return redirect(reverse('auths:my_notify'))
	else :
		return redirect(reverse('main:main'))

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def delete_notifier(request,notify_id):

	# initialize variables
	args={}
	args.update(csrf(request))
	# Quering of objects from model 
	test = Notifier.objects.filter(pk=notify_id)
	# validation 
	if test.count() > 0:
		if test[0].user.username == request.user.username:
			test[0].delete()
			messages.add_message(request, messages.SUCCESS, 'Ваша напоминалка успешно удалена.', fail_silently=True)
		else:
			messages.add_message(request, messages.WARNING, 'Это напоминалка не может быть удалена.', fail_silently=True)
	else:
		messages.add_message(request, messages.WARNING, 'Такой напоминалки не существует. ', fail_silently=True)

	return redirect(reverse('auths:my_notify'))

@login_required(login_url=reverse_lazy('auths:signin'))
def redact_notify(request):
	
	if request.POST:
		# retriving values from form
		min_price = request.POST['from_price']
		max_price = request.POST['to_price']
		notify_id = request.POST['notify_id']

		notify = get_object_or_404(Notifier, pk=notify_id)

		if min_price == '' or int(min_price) < 1 or  max_price == '' or int(max_price) < 1:
			messages.add_message(request, messages.WARNING, 'Пожалуйста укажите суммы правильно.', fail_silently=True)
			return redirect(reverse('auths:my_notify'))
		if notify.user == request.user:
			notify.min_price = min_price
			notify.max_price = max_price
			notify.save()
			messages.add_message(request, messages.SUCCESS, 'Ваша напоминалка успешно отредактирована.', fail_silently=True)
		else:
			messages.add_message(request, messages.WARNING, 'Это напоминалка не может быть отредактирована.')

		return redirect(request.META.get('HTTP_REFERER'))
	
	else :
		return redirect(reverse('main:main'))

@email_required
def search(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args,request)
	# retrieving objects from get request
	start = request.GET.get('start', '')
	end = request.GET.get('end', '')
	exchange = request.GET.get('exchange', '')
	box = request.GET.get('box' , '')
	city = request.GET.get('city', '')
	category = request.GET.get('category', '')
	brand_id = request.GET.get( category , '')
	# validation
	if start == '':
		start = 0
	if end == '':
		end = 100000
	if brand_id == '' or brand_id == 'all_things':
		brand_id = -1
	if brand_id == 'all_brands':
		brand_id = 0
	if brand_id == -1:
		instances = Instance.objects.filter(price__lte=end).filter(price__gte=start).order_by('price')
	elif brand_id == 0:
		instances = Instance.objects.filter(model__brand__category__title=category).filter(price__lte=end).filter(price__gte=start).order_by('price')
	else:
		instances = Instance.objects.filter(model__brand__id=brand_id).filter(price__lte=end).filter(price__gte=start).order_by('price')
	if city and city != 'All':
		city = get_object_or_404(City, name=city)
		instances = instances.filter(city=city)
	else:
		city = ''
	if exchange == 'on':
		instances = instances.filter(exchange=True)
	if box == 'on':
		instances = instances.filter(box=True)

	try:
		current_page = request.get_full_path().split('?')[1].split('&page')[0]
		args['current_page'] = current_page
	except Exception, e:
		pass

	args['num_of_instances'] = instances.count()
	paginator = Paginator(instances, 16)
	page = request.GET.get('page')
	try:
		instances = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		instances = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
 		instances = paginator.page(paginator.num_pages)

	if city :
		args['city'] = city
	if brand_id == -1 : 
		args['this_category'] = "All_type"
	if brand_id == 0:
		args['this_category'] = get_object_or_404(Category, title=category)
	if brand_id > 0:
		brand = Brand.objects.get(pk=brand_id)
	else:
		brand = 'all_brands'

	# Passing arguments
 	
 	args['exchange'] = exchange
 	args['box'] = box
	args['instances'] = instances
	args['start'] = start
	args['end'] = end
	args['cities'] = City.objects.all()
	args['this_brand'] = brand
	args['categories'] = Category.objects.all()

	return render(request, 'fishkas/search.html', args)

def imei(request):
	# initialization of variables
	args={}
	args.update(csrf(request))
	need_for_every(args, request) 
	if request.POST:
		imei = request.POST['imei']
		instances = Imei.objects.filter(imei=imei)
		if instances.count() > 0:
			instance = instances[0].instance
			if instance.user == request.user:
				liked = Wish.objects.filter(instance=instance)
				args['liked'] = liked
			args['instance'] = instance
			args['model'] = model = instance.model
			args['imeied'] = imei
			messages.add_message(request, messages.SUCCESS, 'Это девайс сертифицирован iBox.kg ', fail_silently=True)
			return render(request, 'fishkas/instance2.html', args )
		else:
			messages.add_message(request, messages.WARNING, 'Этот imei не зарегистрирован. ', fail_silently=True)
	return render(request, 'fishkas/imei.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def add_to_wishlist(request, instance_id):
	# initialize variables
	args={}
	args.update(csrf(request))
	for_buy = request.GET.get('operation', '') == 'buy'
	success = False
	# Query objects from model
	if for_buy:
		instance = get_object_or_404(Instance_buy, id=instance_id)
		if not request.user.wish_set.all().filter(instance_buy=instance).exists():
			wish = Wish.objects.create(user=request.user, instance_buy=instance, for_buy=True)
			success = True
	else:
		instance = get_object_or_404(Instance, id=instance_id)
		if not request.user.wish_set.all().filter(instance=instance).exists():
			wish = Wish.objects.create(user=request.user, instance=instance)
			success = True
	
	if success:	
		messages.add_message(request, messages.SUCCESS, 'Объявление успешно добавлено в избранные.', fail_silently=True)

		# new thread
		send_message_thread = threading.Thread(target=send_message, args={instance,request})
		send_message_thread.start()
	

	return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def delete_from_wishlist(request, instance_id):
	#initialize variables
	args={}
	args.update(csrf(request))
	for_buy = request.GET.get('operation', '') == 'buy'
	success = False
	if for_buy:
		instances = get_object_or_404(Instance_buy, id=instance_id)
		get_object_or_404(Wish, instance_buy=instances, user__username=request.user.username).delete()
		success = True
	else:
		instances = get_object_or_404(Instance, id=instance_id)
		get_object_or_404(Wish, instance=instances, user__username=request.user.username).delete()
		success = True

	if success:
		messages.add_message(request, messages.SUCCESS, 'Избранные объявление успешно удалено.', fail_silently=True)
	return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url=reverse_lazy('auths:signin'))
def up(request, instance_id, sell_or_buy):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args,request)
	# Query objects form model
	if sell_or_buy == 'sell':
		instance = Instance.objects.filter(pk=instance_id)
	else:
		instance = Instance_buy.objects.filter(pk=instance_id)
	# validation
	if instance.count() > 0 and instance[0].user == request.user:
		status = instance[0].update_date()
		if status == "Тема успешно обновлена!":
			messages.add_message(request, messages.SUCCESS, status, fail_silently=True)
		else :
			messages.add_message(request, messages.WARNING, status, fail_silently=True)
		model = instance[0].model
		args['model'] = model
		args['instance'] = instance[0]
	else:
		if instance.count() > 0:
			model = instance[0].model
			args['model'] = model
			args['instance'] = instance[0]
			messages.add_message(request, messages.WARNING, 'Вы не можете обновить это объявление', fail_silently=True)

		else:
			return redirect(reverse('main:main'))

	return redirect(request.META.get('HTTP_REFERER'))

def message(request):
	# initialization of variables
	args={}
	args.update(csrf(request))

	if request.POST:

		message = request.POST['message']
		username = request.POST.get('username', '')
		message = Message.objects.create(message=message, username=username)
		messages.add_message(request, messages.SUCCESS, 'Ваше сообщение успешно отправлено.', fail_silently=True)
		return redirect(request.META.get('HTTP_REFERER'))
	else:
		return redirect(reverse('main:main'))

def send_message(instance, request):
	send_mail('iBox.kg ' + str(instance) ,'Здравствуйте  '+ str(instance.user.first_name) +', Пользователь '+ str(request.user.username) + ' добавил ваше объявление в избранные. Попробуйте связаться с этим пользователем, это ваш потенциальный покупатель. Проверь http://ibox.kg/instance/'+ str(instance.id) , settings.EMAIL_HOST_USER, [instance.user.email], fail_silently=True)


