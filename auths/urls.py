from django.conf.urls import patterns, include, url

urlpatterns = [

    url(r'^signin$', 'auths.views.signin', name='signin'),
    url(r'^signup$', 'auths.views.signup', name='signup'),
    url(r'^signout$', 'auths.views.signout', name='signout'),
    url(r'^profile/modify_profile/$', 'auths.views.modify_profile', name='modify_profile'),
    url(r'^profile/change_password/$', 'auths.views.change_password', name='change_password'),
    url(r'^modify_myinstance$', 'auths.views.modify_myinstance', name='modify_myinstance'),
    url(r'^delete_myinstance/(?P<instance_id>.+)/(?P<ads>.+)$', 'auths.views.delete_myinstance', name='delete_myinstance'),
    url(r'^profile/$', 'auths.views.profile', name='profile'),
    url(r'^profile_os/(?P<user_id>.+)$', 'auths.views.profile_others', name='profile_others'),
    url(r'^my_ads/$', 'auths.views.myinstances', name='myinstances'),
    url(r'^my_wishlist/$', 'auths.views.my_wishlist', name='my_wishlist'),
]
