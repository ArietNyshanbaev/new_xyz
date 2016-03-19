# import of django core packages
from django.core.context_processors import csrf
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render, render_to_response, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
# import of project models
from .models import Bet, Match
# import of custom writen decorator and views
from custom_code.decorators import email_required
from custom_code.ibox_views import need_for_every

"""
def main(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	args.update(csrf(request))
	# passing arguments
	args['messages'] = list(get_messages(request))
	args['matches'] = Match.objects.all().order_by('pk')[:10]
	args['footback_link'] = "sport:main"

	if request.user and Bet.objects.filter(user__username=request.user.username).count() > 0:
		bet = Bet.objects.filter(user=request.user)[0]
		args['bet'] = bet
		predictions = []
		matches = []
		matches.append(bet.match1)
		matches.append(bet.match2)
		matches.append(bet.match3)
		matches.append(bet.match4)
		matches.append(bet.match5)
		matches.append(bet.match6)
		matches.append(bet.match7)
		matches.append(bet.match8)
		matches.append(bet.match9)
		matches.append(bet.match10)
		predictions.append(bet.match1_prediction)
		predictions.append(bet.match2_prediction)
		predictions.append(bet.match3_prediction)
		predictions.append(bet.match4_prediction)
		predictions.append(bet.match5_prediction)
		predictions.append(bet.match6_prediction)
		predictions.append(bet.match7_prediction)
		predictions.append(bet.match8_prediction)
		predictions.append(bet.match9_prediction)
		predictions.append(bet.match10_prediction)

		args['predictions'] = zip(matches,predictions)

	return render(request, 'sport/main.html', args)
"""

def main(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	try:
		test = Bet.objects.get(user__username=request.user.username)
		return redirect(reverse('sport:detailed_bet', kwargs={'bet_id':test.id} ))
	except Exception, e:
		pass
	return redirect(reverse('sport:list_bets'))
	
	
"""
@login_required(login_url=reverse('auths:signin'))
@email_required
def make_bet(request):
	# initialize variables
	args={}
	args.update(csrf(request))

	# Quering of objects from model 
	matches = Match.objects.all().order_by('pk')[:10]

	if request.POST:
		# retrieving values from request and validating them
		m_1 = int(request.POST.get('m_' + str(matches[0].id), '0'))
		if m_1 < 0 or m_1 > 2 :
			m_1 = 0

		m_2 = int(request.POST.get('m_' + str(matches[1].id), '0'))
		if m_2 < 0 or m_2 > 2 :
			m_2 = 0

		m_3 = int(request.POST.get('m_' + str(matches[2].id), '0'))
		if m_3 < 0 or m_3 > 2 :
			m_3 = 0

		m_4 = int(request.POST.get('m_' + str(matches[3].id), '0'))
		if m_4 < 0 or m_4 > 2 :
			m_4 = 0

		m_5 = int(request.POST.get('m_' + str(matches[4].id), '0'))
		if m_5 < 0 or m_5 > 2 :
			m_5 = 0

		m_6 = int(request.POST.get('m_' + str(matches[5].id), '0'))
		if m_6 < 0 or m_6 > 2 :
			m_6 = 0

		m_7 = int(request.POST.get('m_' + str(matches[6].id), '0'))
		if m_7 < 0 or m_7 > 2 :
			m_7 = 0

		m_8 = int(request.POST.get('m_' + str(matches[7].id), '0'))
		if m_8 < 0 or m_8 > 2 :
			m_8 = 0

		m_9 = int(request.POST.get('m_' + str(matches[8].id), '0'))
		if m_9 < 0 or m_9 > 2 :
			m_9 = 0

		m_10 = int(request.POST.get('m_' + str(matches[9].id), '0'))
		if m_10 < 0 or m_10 > 2 :
			m_10 = 0

		bet = Bet.objects.create(user=request.user, match1_prediction=m_1, match2_prediction=m_2, match3_prediction=m_3, 
			match4_prediction=m_4, match5_prediction=m_5, match6_prediction=m_6, match7_prediction=m_7, match8_prediction=m_8, 
			match9_prediction=m_9, match10_prediction=m_10, match1=matches[0], match2=matches[1], match3=matches[2], match4=matches[3],
			match5=matches[4], match6=matches[5], match7=matches[6], match8=matches[7], match9=matches[8], match10=matches[9] )
		bet.save()
		
		messages.add_message(request, messages.SUCCESS, 'Ваша ставка принята', fail_silently=True)

		return redirect(reverse('sport:main'))

@login_required(login_url=reverse('auths:signin'))
def edit_bet(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	# Quering of objects from model 
	bet = get_object_or_404(Bet, user__username = request.user.username)
	matches = Match.objects.all().order_by('pk')[:10]

	# retrieving values from request and validating them
	if request.POST and request.user.username == bet.user.username:
		m_1 = int(request.POST.get('m_' + str(bet.match1.id), '0'))
		if m_1 < 0 or m_1 > 2 :
			m_1 = 0
		bet.match1_prediction = m_1

		m_2 = int(request.POST.get('m_' + str(bet.match2.id), '0'))
		if m_2 < 0 or m_2 > 2 :
			m_2 = 0
		bet.match2_prediction = m_2

		m_3 = int(request.POST.get('m_' + str(bet.match3.id), '0'))
		if m_3 < 0 or m_3 > 2 :
			m_3 = 0
		bet.match3_prediction = m_3

		m_4 = int(request.POST.get('m_' + str(bet.match4.id), '0'))
		if m_4 < 0 or m_4 > 2 :
			m_4 = 0
		bet.match4_prediction = m_4

		m_5 = int(request.POST.get('m_' + str(bet.match5.id), '0'))
		if m_5 < 0 or m_5 > 2 :
			m_5 = 0
		bet.match5_prediction = m_5

		m_6 = int(request.POST.get('m_' + str(bet.match6.id), '0'))
		if m_6 < 0 or m_6 > 2 :
			m_6 = 0
		bet.match6_prediction = m_6

		m_7 = int(request.POST.get('m_' + str(bet.match7.id), '0'))
		if m_7 < 0 or m_7 > 2 :
			m_7 = 0
		bet.match7_prediction = m_7

		m_8 = int(request.POST.get('m_' + str(bet.match8.id), '0'))
		if m_8 < 0 or m_8 > 2 :
			m_8 = 0
		bet.match8_prediction = m_8

		m_9 = int(request.POST.get('m_' + str(bet.match9.id), '0'))
		if m_9 < 0 or m_9 > 2 :
			m_9 = 0
		bet.match9_prediction = m_9

		m_10 = int(request.POST.get('m_' + str(bet.match10.id), '0'))
		if m_10 < 0 or m_10 > 2 :
			m_10 = 0
		bet.match10_prediction = m_10

		bet.save()
		messages.add_message(request, messages.SUCCESS, 'Ваша ставка отредактирована', fail_silently=True)

		return redirect(reverse('sport:main'))
"""

@login_required(login_url=reverse('auths:signin'))
def check_bet(request):
	# Quering of objects from model 
	bets = Bet.objects.all()
	matches = Match.objects.all().order_by('pk')[:10]
	# validation
	if request.user.username == 'ari':
		for bet in bets:
			bet.over_all_result = 0
			if bet.match1_prediction == matches[0].result:
				bet.over_all_result += 1

			if bet.match2_prediction == matches[1].result:
				bet.over_all_result += 1

			if bet.match3_prediction == matches[2].result:
				bet.over_all_result += 1

			if bet.match4_prediction == matches[3].result:
				bet.over_all_result += 1

			if bet.match5_prediction == matches[4].result:
				bet.over_all_result += 1

			if bet.match6_prediction == matches[5].result:
				bet.over_all_result += 1

			if bet.match7_prediction == matches[6].result:
				bet.over_all_result += 1

			if bet.match8_prediction == matches[7].result:
				bet.over_all_result += 1

			if bet.match9_prediction == matches[8].result:
				bet.over_all_result +=1

			if bet.match10_prediction == matches[9].result:
				bet.over_all_result += 1
			
			bet.save()

			messages.add_message(request, messages.SUCCESS, 'Проверка закончена ', fail_silently=True)

		return redirect(reverse('sport:main'))

def list_bets(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args, request)
	
	# Passing arguments
	args['bets'] = Bet.objects.all().order_by('-over_all_result').order_by('date')

	return render(request, 'sport/list_bets.html', args)

def detailed_bet(request, bet_id):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args, request)
	# Query objects from model
	bet = get_object_or_404(Bet, pk=bet_id)
	# Passing arguments
	args['bet'] = bet
	args['user'] = request.user

	predictions = []
	matches = []
	matches.append(bet.match1)
	matches.append(bet.match2)
	matches.append(bet.match3)
	matches.append(bet.match4)
	matches.append(bet.match5)
	matches.append(bet.match6)
	matches.append(bet.match7)
	matches.append(bet.match8)
	matches.append(bet.match9)
	matches.append(bet.match10)
	predictions.append(bet.match1_prediction)
	predictions.append(bet.match2_prediction)
	predictions.append(bet.match3_prediction)
	predictions.append(bet.match4_prediction)
	predictions.append(bet.match5_prediction)
	predictions.append(bet.match6_prediction)
	predictions.append(bet.match7_prediction)
	predictions.append(bet.match8_prediction)
	predictions.append(bet.match9_prediction)
	predictions.append(bet.match10_prediction)

	args['predictions'] = zip(matches,predictions)

	return render(request, 'sport/detailed_bet.html', args)

def rules(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args, request)

	return render(request, 'sport/rules.html', args)

def prize(request):
	# initialize variables
	args={}
	args.update(csrf(request))
	need_for_every(args, request)

	return render(request, 'sport/prize.html', args)

def make_bet_rd(request):

	return redirect(reverse('sport:main'))
