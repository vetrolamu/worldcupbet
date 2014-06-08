from django.conf.urls import patterns, include, url
from bets import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worldcupbet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<game_id>\d+)/$', views.bet, name='detail'),
    url(r'^(?P<game_id>\d+)/save$', views.save_bet, name='save_bet'),
    url(r'^overall', views.overall, name='overall')
)