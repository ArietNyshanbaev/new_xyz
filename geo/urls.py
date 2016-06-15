from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^cattle_track$', 'geo.views.mal_track', name='mal_track'),
]
