from django.shortcuts import render
from .models import CertifiedDevice, Photo, Order
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import OrderForm
from main.models import Instance
from django.core.mail import send_mail
from django.conf import settings
from custom_code.ibox_views import need_for_every
from django.contrib import messages
# Create your views here.
def devices(request):
	args = {}
	need_for_every(args, request)
	args['devices'] = CertifiedDevice.objects.all()
	return render(request, 'certification/devices.html', args)

def certification(request):
	args = {}
	need_for_every(args, request)
	return render(request, 'certification/certification.html', args)

def detailed(request, device_id):
	args = {}
	device_id = int(device_id)
	need_for_every(args, request)
	args['device'] = get_object_or_404(CertifiedDevice, pk=device_id)
	return render(request, 'certification/detailed.html', args)

def order_device(request):
	args = {}
	form = OrderForm()

	if request.POST:
		device_id = request.POST.get('device_id', '')
		form = OrderForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			order = Order.objects.create(email=cd['email'], number=cd['number'], note=cd['note'])
			order.device_id = device_id
			order.save()
			send_mail('iBox.kg Order' ,'Здравствуйте  Поступил заказ Ариет', settings.EMAIL_HOST_USER, ['kira.1sp@gmail.com'], fail_silently=True)
			messages.info(request, 'Ваша заявка принята наши операторы скоро свяжутся с вами.')
			return redirect(reverse('certification:certification'))
	need_for_every(args, request)
	args['form'] = form
	return render(request, 'certification/order_device.html', args)

	