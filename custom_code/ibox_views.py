from fishkas.models import Wish
from django.contrib.messages import get_messages

def need_for_every(args, request):
	""" This function does everything usual that is needed for evert def """
	
	args['user'] = request.user

	test = request.session.get('test_popup', 'no')
	if test == 'no':
		request.session.__setitem__('test_popup', 'yes')
		args['test_popup'] = 1;

	if request.user.is_authenticated():
		user_wish = Wish.objects.filter(user=request.user)
		temp = []
		for wish in user_wish:
			temp.append(wish.instance)
		args['user_wish'] = temp
	# dealing with messages
	args['messages'] = list(get_messages(request))
	return args