# import dealing with encoding of content
from __future__ import unicode_literals
import threading
import urllib2
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
# standart django and core lybraries import
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
# import of custom writen decorator and views
from custom_code.decorators import email_required
from custom_code.ibox_views import need_for_every, notify_me
# import of models 
from .models import Category , Instance , Brand , Modell, Sold, City, Instance_buy
from fishkas.models import Notifier, Wish, Best_deal

@email_required
def main(request):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request)
	# Quering of objects from model 
	category_smartphones = get_object_or_404(Category, title='Телефоны')
	category_notebooks = get_object_or_404(Category, title='Ноутбуки')
	category_tablets = get_object_or_404(Category, title='Планшеты')
	category_accessories = get_object_or_404(Category, title='Аксессуары')
	# Passing arguments
	args['smartphone_offers'] = Instance.objects.filter(model__brand__category=category_smartphones).count()
	args['notebook_offers'] = Instance.objects.filter(model__brand__category=category_notebooks).count()
	args['tablet_offers'] = Instance.objects.filter(model__brand__category=category_tablets).count()
	args['accessory_offers'] = Instance.objects.filter(model__brand__category=category_accessories).count()
	args['category_smartphones'] = category_smartphones
	args['category_notebooks'] = category_notebooks
	args['category_tablets'] = category_tablets
	args['category_accessories'] = category_accessories
	args['categories'] = Category.objects.all()
	args['instances'] = Instance.objects.all().order_by("-updated_date")[:16]
	args['instances_to_buy'] = Instance_buy.objects.all().order_by("-updated_date")[:16]
	args['best_deals'] = Best_deal.objects.all()

	return render(request, 'main/main.html', args)

@email_required
def category(request, category_id):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request)

	# Quering of objects from model 
	this_category = get_object_or_404(Category, pk=category_id)
	instances = Instance.objects.filter(model__brand__category=this_category).order_by('-updated_date')
	instances_to_buy = Instance_buy.objects.filter(model__brand__category=this_category).order_by('-updated_date')

	# Pagination
	paginator = Paginator(instances, 20)
	
	page = request.GET.get('page')
	

	try:
		instances = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		instances = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
 		instances = paginator.page(paginator.num_pages)

 	paginator_buy = Paginator(instances_to_buy, 20)
 	page_buy = request.GET.get('page_buy')
 		
 	try:
 		instances_to_buy = paginator_buy.page(page_buy)
 	except PageNotAnInteger:
 		# If page is not an integer, deliver first page.
 		instances_to_buy = paginator_buy.page(1)
 	except EmptyPage:
 		# If page is out of range (e.g. 9999), deliver last page of results.
 		instances_to_buy = paginator_buy.page(paginator_buy.num_pages)
 	

 	# Passing arguments
 	args['categories'] = Category.objects.all()
	args['instances'] = instances
	args['instances_to_buy'] = instances_to_buy
	args['brands'] = this_category.brand_set.all().order_by('title')
	args['this_category'] = this_category

	return render(request, 'main/category.html', args)

@email_required
def brand(request, brand_id):
	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request)
	# Quering of objects from model 
	brand = get_object_or_404(Brand, pk=brand_id)
	instances = Instance.objects.filter(model__brand=brand).order_by('-updated_date')
	instances_to_buy = Instance_buy.objects.filter(model__brand=brand).order_by('-updated_date')
	
	# Pagination
	paginator = Paginator(instances, 20)
	page = request.GET.get('page')

	try:
		instances = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		instances = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
 		instances = paginator.page(paginator.num_pages)

 	paginator_buy = Paginator(instances_to_buy, 20)
 	page_buy = request.GET.get('page_buy')

 	try:
 		instances_to_buy = paginator_buy.page(page_buy)
 	except PageNotAnInteger:
 		# If page is not an integer, deliver first page.
 		instances_to_buy = paginator_buy.page(1)
 	except EmptyPage:
 		# If page is out of range (e.g. 9999), deliver last page of results.
 		instances_to_buy = paginator_buy.page(paginator_buy.num_pages)

 	# Passing arguments
	args['brand'] = brand
	args['models'] =  brand.modell_set.all().order_by('title')
	args['instances'] = instances
	args['instances_to_buy'] = instances_to_buy
	args['categories'] = Category.objects.all()

	return render(request, 'main/brand.html', args)

@email_required
def model(request, model_id):

	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args,request)
	# Quering of objects from model 
	this_model = get_object_or_404(Modell, pk=model_id)
	instances = Instance.objects.filter(model = this_model).order_by('-updated_date')
	instances_to_buy = Instance_buy.objects.filter(model = this_model).order_by('-updated_date')

	# Passing arguments
	paginator = Paginator(instances, 20)
	page = request.GET.get('page')
	try:
		instances = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		instances = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
 		instances = paginator.page(paginator.num_pages)

 	paginator_buy = Paginator(instances_to_buy, 20)
 	page_buy = request.GET.get('page_buy')

 	try:
 		instances_to_buy = paginator_buy.page(page_buy)
 	except PageNotAnInteger:
 		# If page is not an integer, deliver first page.
 		instances_to_buy = paginator_buy.page(1)
 	except EmptyPage:
 		# If page is out of range (e.g. 9999), deliver last page of results.
 		instances_to_buy = paginator_buy.page(paginator_buy.num_pages)

 	# Passing arguments
	args['models'] = this_model.brand.modell_set.all().order_by('title')
	args['instances'] = instances
	args['instances_to_buy'] = instances_to_buy
	args['this_model'] = this_model
	args['user'] = request.user
	args['categories'] = Category.objects.all()

	return render(request, 'main/model.html',args)

@email_required
def instance(request, instance_id):

	#initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request) 
	operation = request.GET.get('operation', '')

	# Quering of objects from model 
	if operation == 'buy':
		instance = get_object_or_404(Instance_buy, pk=instance_id)
		args['similar_instances'] = Instance_buy.objects.filter(model=instance.model).order_by('-updated_date').exclude(pk=instance_id)[:4]
		template = 'main/instance_buy.html'
	else:
		instance = get_object_or_404(Instance, pk=instance_id)
		args['similar_instances'] = Instance.objects.filter(model=instance.model).order_by('-updated_date').exclude(pk=instance_id)[:4]
		template = 'main/instance.html'

	#if instance.user == request.user:
	#	liked = Wish.objects.filter(instance=instance)
	#	args['liked'] = liked
	
	# Passing arguments
	
	args['model'] = model = instance.model
	args['instance'] = instance
	args['user'] = request.user

	return render(request, template, args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def add_instance_phones(request):

	# initialize variables
	args = {}
	args.update(csrf(request))
	need_for_every(args, request)

	if request.POST:
		# retriving values from form
		city = request.POST.get('city', '')
		link = request.POST.get('link', '')
		title = request.POST.get('title', '')
		brand = request.POST.get('brand', '')
		color = request.POST.get('color', '')
		telephone = request.POST.get('telephone', '')
		note = request.POST.get('note', '')
		price = request.POST.get('price', '')
		photo1 = request.FILES.get('photo1', '')
		photo2 = request.FILES.get('photo2', '')
		photo3 = request.FILES.get('photo3', '')
		memory = request.POST.get('memory', '')
		condition = request.POST.get('condition', '')
		guarantee = request.POST.get('guarantee', '')
		earpods = request.POST.get('earpods', '')
		box = request.POST.get('box', '')
		exchange = request.POST.get('exchange', '')
		bargain = request.POST.get('bargain', '')
		# validation
		if len(title) > 80:
			title = title[:80]
		if earpods == '1':
			earpods = True
		else:
			earpods = False
		if box == '1':
			box = True
		else:
			box = False
		if exchange == '1':
			exchange = True
		else:
			exchange = False
		if bargain == '1':
			bargain = True
		else:
			bargain = False

		model_id = request.POST.get(brand,'')
		model_id = model_id.split('_')[0]

		model = get_object_or_404(Modell, pk=model_id)
		if city:
			city = City.objects.filter(name=city)[0]

		if model.is_not_unique == True:
			brand_unique = brand + '_unique'
			modell = request.POST.get(brand_unique, '')
			instance = Instance.objects.create(linker=link, title=title, color=color, memory=memory, condition=condition, guarantee=guarantee, smartphone=True, earpods=earpods, box=box, exchange=exchange, bargain=bargain, user=request.user, telephones=telephone, note=note, photo1 = photo1, photo2 = photo2, photo3 = photo3, price=price, model=model, modell=modell, city=city)
		else:
			instance = Instance.objects.create(linker=link, title=title, color=color, memory=memory, condition=condition, guarantee=guarantee, smartphone = True,earpods = earpods, box = box,exchange = exchange, bargain = bargain,user=request.user, telephones=telephone, note=note, photo1=photo1, photo2=photo2, photo3=photo3, price=price, model=model, city=city)
		instance.save()
		messages.add_message(request, messages.SUCCESS, "Ваше объявление успешно создано", fail_silently=True)
		# part of notify me
		notifier = threading.Thread(target=notify_me, args={instance,})
		notifier.start()

		return redirect(reverse('auths:myinstances'))
	# Quering of objects from model 
	category = get_object_or_404(Category, title="Телефоны")
	# Passing arguments
	args['brands'] = category.brand_set.all()
	args['cities'] = City.objects.all()

	return render(request, 'main/add_instance_phones.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def add_instance_notebooks(request):

	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args, request)

	if request.POST:
		# retriving values from form
		city = request.POST.get('city', '')
		link = request.POST.get('link', '')
		title = request.POST.get('title', '')
		brand = request.POST.get('brand', '')
		color = request.POST.get('color', '')
		telephone = request.POST.get('telephone', '')
		note = request.POST.get('note', '')
		price = request.POST.get('price', '')
		photo1 = request.FILES.get('photo1', '')
		photo2 = request.FILES.get('photo2', '')
		photo3 = request.FILES.get('photo3', '')
		condition = request.POST.get('condition', '')
		guarantee = request.POST.get('guarantee', '')
		box = request.POST.get('box', '')
		exchange = request.POST.get('exchange', '')
		bargain = request.POST.get('bargain', '')
		# Validation
		if len(title) > 80:
			title = title[:80]
		if box == '1':
			box = True
		else:
			box = False
		if exchange == '1':
			exchange = True
		else:
			exchange = False
		if bargain == '1':
			bargain = True
		else:
			bargain = False
		if city:
			city = City.objects.filter(name=city)[0]

		model_id = request.POST.get(brand, '')
		model = get_object_or_404(Modell, pk=model_id)
		instance = Instance.objects.create(linker=link, title=title, color=color, condition=condition, guarantee=guarantee, notebook=True, box=box, exchange=exchange, bargain=bargain, user=request.user, telephones=telephone, note=note, photo1=photo1, photo2=photo2, photo3=photo3, price=price, model=model, city=city)
		instance.save()
		messages.add_message(request, messages.SUCCESS, "Ваше объявление успешно создано", fail_silently=True)
		# part of notify me
		notifier = threading.Thread(target=notify_me, args={instance,})
		notifier.start()
		
		return redirect(reverse('auths:myinstances'))
	# Quering of objects from model 
	category = get_object_or_404(Category, title="Ноутбуки")
	# Passing arguments
	args['brands'] =  category.brand_set.all()
	args['cities'] = City.objects.all()

	return render(request, 'main/add_instance_notebooks.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def add_instance_tablets(request):

	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args,request)

	if request.POST:
		# retriving values from form
		city = request.POST.get('city', '')
		link = request.POST.get('link', '')
		title = request.POST.get('title', '')
		brand = request.POST.get('brand', '')
		color = request.POST.get('color', '')
		note = request.POST.get('note', '')
		price = request.POST.get('price', '')
		telephone = request.POST.get('telephone', '')
		photo1 = request.FILES.get('photo1', '')
		photo2 = request.FILES.get('photo2', '')
		photo3 = request.FILES.get('photo3', '')
		condition = request.POST.get('condition', '')
		guarantee = request.POST.get('guarantee', '')
		memory = request.POST.get('memory', '')
		box = request.POST.get('box', '')
		exchange = request.POST.get('exchange', '')
		bargain = request.POST.get('bargain', '')

		# Validation
		if len(title) > 80:
			title = title[:80]
		if box == '1':
			box = True
		else:
			box = False
		if exchange == '1':
			exchange = True
		else:
			exchange = False
		if bargain == '1':
			bargain = True
		else:
			bargain = False
		if city:
			city = City.objects.filter(name=city)[0]

		model_id = request.POST.get(brand, '')
		model = get_object_or_404(Modell, pk=model_id)
		instance = Instance.objects.create(linker=link, title=title, memory=memory, color=color, condition=condition, guarantee=guarantee, tablet=True, box=box, exchange=exchange, bargain=bargain, user=request.user, telephones=telephone, note=note, photo1=photo1, photo2=photo2, photo3=photo3, price=price, model=model, city=city)
		instance.save()
		messages.add_message(request, messages.SUCCESS, "Ваше объявление успешно создано", fail_silently=True)
		# part of notify me
		notifier = threading.Thread(target=notify_me, args={instance,})
		notifier.start()
 
		return redirect(reverse('auths:myinstances'))
	# Quering of objects from model 
	category = get_object_or_404(Category, title="Планшеты")
	# Passing arguments
	args['brands'] = category.brand_set.all()
	args['user'] = request.user
	args['cities'] = City.objects.all()
	return render(request, 'main/add_instance_tablets.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def add_instance_accessories(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args,request)

	if request.POST:
		# retriving values from form
		city = request.POST.get('city', '')
		link = request.POST.get('link', '')
		title = request.POST.get('title', '')
		brand = request.POST.get('brand', '')
		color = request.POST.get('color', '')
		note = request.POST.get('note', '')
		price = request.POST.get('price', '')
		telephone = request.POST.get('telephone', '')
		photo1 = request.FILES.get('photo1', '')
		photo2 = request.FILES.get('photo2', '')
		photo3 = request.FILES.get('photo3', '')
		condition = request.POST.get('condition', '')
		guarantee = request.POST.get('guarantee', '')
		memory = request.POST.get('memory', '')
		box = request.POST.get('box', '')
		exchange = request.POST.get('exchange', '')
		bargain = request.POST.get('bargain', '')
		# validation
		if len(title) > 80:
			title = title[:80]
		if box == '1':
			box = True
		else:
			box = False
		if exchange == '1':
			exchange = True
		else:
			exchange = False
		if bargain == '1':
			bargain = True
		else:
			bargain = False
		if city:
			city = City.objects.filter(name=city)[0]

		model_id = request.POST.get(brand, '')
		model = get_object_or_404(Modell, pk=model_id)
		instance = Instance.objects.create(linker=link, title=title, memory=memory, color=color, condition=condition, guarantee=guarantee, other=True, box=box, exchange=exchange, bargain=bargain, user=request.user, telephones=telephone, note=note, photo1=photo1, photo2=photo2, photo3=photo3, price=price, model=model, city=city)
		instance.save()
		messages.add_message(request, messages.SUCCESS, "Ваше объявление успешно создана",fail_silently=True)
		# part of notify me
		notifier = threading.Thread(target=notify_me, args={instance,})
		notifier.start()
		
		return redirect(reverse('auths:myinstances'))

	# Quering of objects from model 
	category = get_object_or_404(Category, title="Аксессуары")
	# Passing arguments
	args['brands'] = category.brand_set.all()
	args['cities'] = City.objects.all()
	return render(request, 'main/add_instance_accessories.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
@email_required
def add_buy_instance(request, type):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args,request)

	if request.POST:
		# retriving values from form
		city = request.POST.get('city', '')
		title = request.POST.get('title', '')
		brand = request.POST.get('brand', '')
		price = request.POST.get('price', '')
		telephone = request.POST.get('telephone', '')
		note = request.POST.get('note', '')
		model_id = request.POST.get(brand, '')

		model_id = model_id.split('_')[0]
		model = get_object_or_404(Modell, pk=model_id)

		# validation
		if len(title) > 80:
			title = title[:80]
		if city:
			city = City.objects.filter(name=city)[0]
		buy_instance = Instance_buy.objects.create(title=title, user=request.user, telephones=telephone, note=note, price=price, model=model, city=city)
		if type == 'smartphone':
			buy_instance.smartphone = True
		elif type == 'notebook':
			buy_instance.notebook = True
		elif type == 'tablet':
			buy_instance.tablet = True
		else:
			buy_instance.other = True
		buy_instance.save()
		messages.add_message(request, messages.SUCCESS, "Ваше объявление успешно создана", fail_silently=True)
		# part of notify me
		# notifier = threading.Thread(target=notify_me, args={instance,})
		# notifier.start()
		
		return redirect(reverse('auths:myinstances'))

	# Quering of objects from model 
	if type == 'smartphone':
		category = get_object_or_404(Category, title='Телефоны')
	elif type == 'notebook':
		category = get_object_or_404(Category, title='Ноутбуки')
	elif type == 'tablet':
		category = get_object_or_404(Category, title='Планшеты')
	elif type == 'accessories':
		category = get_object_or_404(Category, title='Аксессуары')
	else:
		category = get_object_or_404(Category, title=type)
	# Passing arguments
	args['brands'] = category.brand_set.all()
	args['cities'] = City.objects.all()
	args['category'] = category.title[:-1]

	return render(request, 'main/add_buy_instance.html', args)

def delete_from_diesel(request):
	# initialize variables
	args = {}
	# validation
	if request.user.username == 'ari':
		counter = 0
		# Query of diesel's instances from model
		instances = Instance.objects.filter(user__username='diesel')
		for instance in instances:
			response = urllib2.urlopen(instance.linker)
			html = response.read()
			html = unicode(html, errors='ignore')
			
			if html.find('class="errorwrap"') != -1:
				instance.delete()
				Sold.objects.create(seller = request.user, date_added=instance.added_date, price=instance.price, model=instance.model, sold_at_ibox=False)
				counter = counter + 1
			else:
				continue
		# Passing arguments
		args['counter'] = counter
		need_for_every(args, request)
		return render(request, 'main/delete_from_diesel.html', args)
	else:
		return redirect(reverse('main:main'))


def check_diesel(request):
	if request.POST:
		link = request.POST.get('link', '')
		if Instance.objects.filter(linker=link).count() > 0:
			messages.add_message(request, messages.WARNING, 'Добавлять нельзя , данное объявление уже существует.',fail_silently=True)
		else:
			messages.add_message(request, messages.SUCCESS, 'Можно добавлять',fail_silently=True)
			
	return redirect(request.META.get('HTTP_REFERER'))


