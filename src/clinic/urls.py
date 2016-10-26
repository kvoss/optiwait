from django.conf.urls import patterns, url

from clinic import views

urlpatterns = patterns('',
    url(r'', views.index, name='index'),
)


