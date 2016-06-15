#importings
from __future__ import unicode_literals
import threading
import urllib2
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
import datetime
from django.utils.timezone import utc
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from main.models import Category , Instance , Brand , Modell, Sold, City
from fishkas.models import Notifier, Slogan, Wish, Best_deal
from postman.models import Message
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.messages import get_messages
from django.template import RequestContext
#impoer of models 

from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url=reverse_lazy('auths:signin'))
def main(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	my_date = datetime.datetime.now().utcnow().replace(tzinfo=utc) - datetime.timedelta(days=1)
	args['date'] = my_date + datetime.timedelta(days=1)
	args['users'] = User.objects.filter(date_joined__gte = my_date).count()
	args['messages'] = Message.objects.filter(sent_at__gte = my_date).count()
	args['sold'] = Sold.objects.filter(date__gte = my_date).exclude(seller__username='ari').count()
	args['ads'] = Instance.objects.filter(added_date__gte = my_date).exclude(user__username='diesel').count()


	
	return render_to_response('adminka/index.html', args)
@login_required(login_url=reverse_lazy('auths:signin'))
def detail_ads(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	list_days = []
	list_date = []

	my_date = datetime.datetime.now().replace(hour = 0,minute = 1)

	for i in range(31,-1,-1):
		date = my_date - datetime.timedelta(days = i)
		date2 = date + datetime.timedelta(days = 1)
		list_date.append(date)
		list_days.append(Instance.objects.filter(added_date__gte = date).filter(added_date__lt = date2).exclude(user__username='diesel').count())
	
	zipped_list = zip(list_days, list_date)
	args['zipped_list'] = zipped_list
	args['date'] = datetime.datetime.now()
	
	return render_to_response('adminka/detail_ads.html', args)

@login_required(login_url=reverse_lazy('auths:signin'))
def detail_user(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	list_days = []
	list_date = []

	my_date = datetime.datetime.now().replace(hour = 0,minute = 0)

	for i in range(31,-1,-1):
		date = my_date - datetime.timedelta(days = i)
		date2 = date + datetime.timedelta(days = 1)
		list_date.append(date)
		list_days.append(User.objects.filter(date_joined__gte = date.date).filter(date_joined__lt = date2).count())

	zipped_list = zip(list_days, list_date)
	args['zipped_list'] = zipped_list
	args['date'] = datetime.datetime.now()

	return render_to_response('adminka/detail_user.html', args)
@login_required(login_url=reverse_lazy('auths:signin'))
def detail_message(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	list_days = []
	list_date = []

	my_date = datetime.datetime.now().replace(hour = 0,minute = 0)

	for i in range(31,-1,-1):
		date = my_date - datetime.timedelta(days = i)
		date2 = date + datetime.timedelta(days = 1)
		list_date.append(date)
		list_days.append(Message.objects.filter(sent_at__gte = date.date).filter(sent_at__lt = date2).count())

	zipped_list = zip(list_days, list_date)
	args['zipped_list'] = zipped_list
	args['date'] = datetime.datetime.now()
	
	return render_to_response('adminka/detail_message.html', args)
@login_required(login_url=reverse_lazy('auths:signin'))
def detail_sold(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	list_days = []
	list_date = []

	my_date = datetime.datetime.now().replace(hour = 0,minute = 0)
	
	for i in range(31,-1,-1):
		date = my_date - datetime.timedelta(days = i)
		date2 = date + datetime.timedelta(days = 1)
		list_date.append(date)
		list_days.append(Sold.objects.filter(date__gte = date.date).filter(date__lt = date2).exclude(seller__username='ari').count())
	
	zipped_list = zip(list_days, list_date)
	args['zipped_list'] = zipped_list
	args['date'] = datetime.datetime.now()
	
	return render_to_response('adminka/detail_sold.html', args)