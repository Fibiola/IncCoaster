from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'landing.views.home', name='home'),
    url(r'^sendContact$', 'landing.views.contact', name='home'),
    url(r'^thanks$', 'landing.views.thanks', name='thanks'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
