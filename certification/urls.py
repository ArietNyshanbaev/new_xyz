from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^$', 'certification.views.certification', name='certification'),
    url(r'^devices$', 'certification.views.devices', name='devices'),
    url(r'^detailed/(?P<device_id>.+)$', 'certification.views.detailed', name='detailed'),
    url(r'^order_device$', 'certification.views.order_device', name='order_device'),
]
