from django.conf.urls import patterns, include, url
from bets import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worldcupbet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bets/', include('bets.urls')),
    url(r'', include('bets.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^accounts/', include('registration.backends.default.urls'))
)
