from django.conf.urls import patterns, include, url
from mtorourke import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mtorourke.views.homepage', name='homepage'),
    url(r'^portfolio/$', 'mtorourke.views.portfolio', name='portfolio'),
    url(r'^contact/$', 'mtorourke.views.contact', name='contact'),
    url(r'^about/$', 'mtorourke.views.about', name='about'),
    url(r'^kalite/$', 'mtorourke.views.kalite', name='kalite'),
    url(r'^ucsd/$', 'mtorourke.views.ucsd', name='ucsd'),
    url(r'^eslgenie/$', 'mtorourke.views.eslgenie', name='eslgenie'),
    url(r'^lindamoodbell/$', 'mtorourke.views.lindamoodbell', name='lindamoodbell'),
    # url(r'^mtorourke/', include('mtorourke.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
	url(r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)