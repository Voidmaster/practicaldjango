from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

from weblog.models import Entry, Artista
from weblog.views import EncuestaActivaView, VotarEncuestaView, ArtistasView, index

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^weblog/index/$', 'weblog.views.index', name='index'),

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
            template_name="weblog/artistas.html",
            paginate_by=10),
            name="artistas"),

    url(r'^weblog/artistas/abc/$',
        ArtistasView.as_view(), name="paginacion_artistas"),

    url(r'^weblog/artistas/(?P<slug>[-\w]+)/$',
        DetailView.as_view(
            model=Artista,
            template_name='weblog/artista_detail.html'),
            name='detalle'),
   
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'search.views.search'),
    url(r'^weblog/encuesta/$', EncuestaActivaView.as_view(), name='encuesta_activa'),
    url(r'^weblog/votar_encuesta/$', VotarEncuestaView.as_view(), name='votar_encuesta'),
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
