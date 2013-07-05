from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

from weblog.models import Entry

from weblog.models import Entry, Artista


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^weblog/$',
    	ListView.as_view(
     		queryset=Entry.objects.all(),
     		context_object_name='entry_list',
     		template_name='weblog/entry_index.html'),
     		name='index'),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
    	DetailView.as_view(
    		model=Entry,
    		template_name='weblog/entry_detail.html'),
    		name='detail'),

    url(r'^weblog/artistas/$',
        ListView.as_view(
            queryset=Artista.objects.all(),
            context_object_name='artistas',
            template_name="weblog/artistas.html"),
            name="artistas"),

   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'search.views.search'),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
