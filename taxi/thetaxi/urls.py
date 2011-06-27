from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'thetaxi.views.home'),
    url(r'^details/$', 'thetaxi.views.taxi_details'),
    url(r'^add/$', 'blog.views.add'),

)
