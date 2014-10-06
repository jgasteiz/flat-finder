from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    'public.views',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'home', name='home'),
)
