from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^clinic/', include('clinic.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'optiwait.views.home', name='home'),
)

