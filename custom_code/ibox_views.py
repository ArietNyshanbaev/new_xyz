from fishkas.models import Wish
from django.contrib.messages import get_messages
from fishkas.models import Notifier
from django.core.mail import send_mail

def need_for_every(args, request):
	""" This function does everything usual that is needed for evert def """

	test = request.session.get('test_popup', 'no')
	if test == 'no':
		request.session.__setitem__('test_popup', 'yes')
		args['test_popup'] = 1;

	if request.user.is_authenticated():
		user_wish = Wish.objects.filter(user=request.user)
		temp = []
		for wish in user_wish:
			if wish.for_buy:
				temp.append(wish.instance_buy)
			else:
				temp.append(wish.instance)
		args['user_wish'] = temp
	# dealing with messages
	args['messages'] = list(get_messages(request))
	return args

def notify_me(instance):
	# part of notify me
	counter = [];
	notifiers = Notifier.objects.all().filter(max_price__gte=instance.price).filter(min_price__lte=instance.price)
	for notifier in notifiers:
		if instance.model.brand.category.title in notifier.categories.split(",") :
			counter.append(notifier.user.email)
	counter = list(set(counter))
	for count in counter:
		send_mail('iBox напоминалка.' ,'Привет '+ get_object_or_404(User,email=count).first_name +', на iBox.kg поступило объявление за '+ str(instance.price) + ' сом, которое заинтересует вас. Проверь http://ibox.kg/instance/'+ str(instance.id) , settings.EMAIL_HOST_USER, [count], fail_silently=True)