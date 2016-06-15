from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from auths.models import Verification 

class CheckEmailMiddleware(object):
	# Check if user has email
	def process_request(self, request):
		if request.user.is_authenticated() and '/auths' not in request.path_info:
			if request.user.email == '':
				request.path_info = reverse('auths:enter_email')
			else:
				verification = Verification.objects.filter(user=request.user)
				if verification.count() > 0:
					if verification[0].is_verified == False:
						request.path_info = reverse('auths:need_to_verify_email')
				else:
					request.path_info = reverse('auths:need_to_verify_email')
		return None
