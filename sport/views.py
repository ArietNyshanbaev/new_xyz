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
