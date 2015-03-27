from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.models import *

from core.views import SongDetailView



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gtg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
 	url(r'^(?P<slug>[-_\w]+)/$', SongDetailView.as_view(), name='song-detail'),
    # url(r'^admin/', include(admin.site.urls)),
)
