from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'thetaxi.views.home'),
    url(r'^details/$', 'thetaxi.views.taxi_details'),
    url(r'^add/$', 'thetaxi.views.add'),
    url(r'^home/$', 'thetaxi.views.home'),

)
