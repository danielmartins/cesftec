from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cesftec.views.home', name='home'),
    url(r'home/$', 'cesftec.cripto.views.home', name='home'),
    url(r'home/(?P<tipo>\w+)/$', 'cesftec.cripto.views.home', name='home_tipo'),
    url(r'home/(?P<tipo>\w+)/decrypt/$', 'cesftec.cripto.views.home_uncrypt', name='home_decrypt'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
