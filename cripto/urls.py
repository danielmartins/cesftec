from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cesftec.views.home', name='home'),
    url(r'cesar/$', 'cesftec.cripto.views.cesar', name='cesar'),
    url(r'cesar/decrypt/$', 'cesftec.cripto.views.cesar_uncrypt', name='cesar_decrypt'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
