from django.conf.urls import patterns, include, url

urlpatterns = [

    url(r'^what_can_i_afford/$', 'fishkas.views.what_can_i_effort', name='what_can_i_effort'),
    url(r'^search/$', 'fishkas.views.search', name='search'),
    url(r'^imei/$', 'fishkas.views.imei', name='imei'),
    url(r'^add_to_wishlist/(?P<instance_id_field>.+)$', 'fishkas.views.add_to_wishlist', name='add_to_wishlist'),
    url(r'^delete_from_wishlist/(?P<instance_id>.+)$', 'fishkas.views.delete_from_wishlist', name='delete_from_wishlist'),
    url(r'^up/(?P<instance_id>.+)/(?P<sell_or_buy>.+)$', 'fishkas.views.up', name='up'),
    url(r'^message/$', 'fishkas.views.message', name='message'),
    url(r'^notify_me/$', 'fishkas.views.notify_me', name='notify_me'),
    url(r'^delete_notifier/(?P<notify_id>.+)$', 'fishkas.views.delete_notifier', name='delete_notifier'),
    url(r'^redact_notify/$', 'fishkas.views.redact_notify', name='redact_notify'),
    
]
