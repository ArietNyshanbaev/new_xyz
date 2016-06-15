from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'main.views.main', name='main'),
    url(r'^category/(?P<category_id>.+)$', 'main.views.category', name='category'),
    url(r'^brand/(?P<brand_id>.+)$', 'main.views.brand', name='brand'),
    url(r'^model/(?P<model_id>.+)$', 'main.views.model', name='model'),
    url(r'^instance/(?P<instance_id>.+)$', 'main.views.instance', name='instance'),
    url(r'^add_instance/phones$', 'main.views.add_instance_phones', name='add_instance_phones'),
    url(r'^add_instance_buy/(?P<type>.+)$', 'main.views.add_buy_instance', name='add_buy_instance'),
    url(r'^add_instance/notebooks$', 'main.views.add_instance_notebooks', name='add_instance_notebooks'),
    url(r'^add_instance/tablets$', 'main.views.add_instance_tablets', name='add_instance_tablets'),
    url(r'^add_instance/accessories$', 'main.views.add_instance_accessories', name='add_instance_accessories'),
    url(r'^add_device$', 'main.views.add_device', name='add_device'),
    url(r'^delete_diesel/$', 'main.views.delete_from_diesel', name='delete_diesel'),
    url(r'^check_diesel/$', 'main.views.check_diesel', name='check_diesel'),
]
