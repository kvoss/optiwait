from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p12.views.home', name='home'),
    url(r'^clinic/', include('clinic.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'p12.views.home', name='home'),
)
