from django.conf.urls import patterns, include, url

urlpatterns = [

    url(r'^$', 'sport.views.main', name='main'),
    #url(r'^make_bet$', 'sport.views.make_bet', name='make_bet'),
    url(r'^make_bet_rd$', 'sport.views.make_bet_rd', name='make_bet_rd'),
    #url(r'^edit_bet$', 'sport.views.edit_bet', name='edit_bet'),
    url(r'^check_bet$', 'sport.views.check_bet', name='check_bet'),
    url(r'^list_bets$', 'sport.views.list_bets', name='list_bets'),
    url(r'^detailed_bet/(?P<bet_id>.+)$', 'sport.views.detailed_bet', name='detailed_bet'),
    url(r'^rules$', 'sport.views.rules', name='rules'),
    url(r'^prize$', 'sport.views.prize', name='prize'),

]