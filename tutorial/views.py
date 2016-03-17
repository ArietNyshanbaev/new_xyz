from django.shortcuts import render
from custom_code.ibox_views import need_for_every

def search(request):
	#initialize variables
	args={}
	need_for_every(args, request)
	
	return render(request, 'tutorial/search.html', args)