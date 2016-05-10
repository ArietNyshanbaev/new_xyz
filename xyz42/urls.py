# django core packages import 
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
# project packeges import
from main.sitemaps import InstanceSitemap
# third party packages import
from ajax_select import urls as ajax_select_urls
admin.autodiscover()

sitemaps = {
       'instances': InstanceSitemap,
}

urlpatterns = [
    url(r'^', include('main.urls', namespace='main')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adminka/', include('adminka.urls', namespace='adminka')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^features/', include('fishkas.urls', namespace='fishkas')),
    url(r'^bet/', include('sport.urls', namespace='sport')),
    url(r'^auths/', include('auths.urls', namespace='auths')),
    url(r'^tutorial/', include('tutorial.urls', namespace='tutorial')),
    url(r'^certification/', include('certification.urls', namespace='certification')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^messages/', include('postman.urls', namespace="postman")),
    url(r'^password_reset/', include('password_reset.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^sitemap.xml', include('static_sitemaps.urls')),
    url(r'^lookups/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
    ]
urlpatterns += [
   url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
]
