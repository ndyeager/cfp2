"""cfp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'cfp.views.home', name='home'),
	url(r'^program/$', 'cfp.views.program', name='program'),
	url(r'^hack_night/', include('hack_night.urls')),
	url(r'^program/$', 'cfp.views.program', name='program'),
	url(r'^alumni/$', 'cfp.views.alumni', name='alumni'),
	url(r'^faq/$', 'cfp.views.faq', name='faq'),
	url(r'^contact/$', 'cfp.views.contact', name='contact'),
	url(r'^staff/$', 'cfp.views.staff', name='staff'),
	url(r'^apply/$', 'cfp.views.apply', name='apply'),
	url(r'^community/$', 'cfp.views.community', name='community'),
	url(r'^partner/$', 'cfp.views.partner', name='partner'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG: 
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    from django.views.static import serve
    from django.conf.urls import patterns
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
