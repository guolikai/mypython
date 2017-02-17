from django.conf.urls import patterns, include, url
from django.contrib import admin
from DynamicRouter.activator import process

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DynamicRouter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    
    ('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\d+))/(?P<id>(\d+))/$',process),
    ('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\d+))/$',process),
    ('^(?P<app>(\w+))/(?P<function>(\w+))/$',process),
    ('^(?P<app>(\w+))/$',process,{'function':'index'}),
)
