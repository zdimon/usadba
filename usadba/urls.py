from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.show',{'alias':'mainpage'}, name='home'),
    #url(r'^page/(?P<alias>\w+)/$', 'main.views.show', None, name='page_link'),
    # url(r'^usadba/', include('usadba.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url('', include('main.urls')),
)
urlpatterns += staticfiles_urlpatterns()