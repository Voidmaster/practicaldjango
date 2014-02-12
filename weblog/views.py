from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from weblog.models import Encuesta, OpcionEncuesta, Artista, Entry
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class EncuestaActivaView(TemplateView):
    template_name = "weblog/encuesta_activa.html"
    
    def get_context_data(self):
      context = super(EncuestaActivaView, self).get_context_data()
      encuestas_activas = Encuesta.objects.filter(activa=True).order_by('fecha_publicacion')
      if encuestas_activas:
          encuesta_activa = encuestas_activas[0]
          opciones_encuesta = OpcionEncuesta.objects.filter(encuesta=encuesta_activa)
          context.update({'opciones_encuesta' : opciones_encuesta, 'encuesta_activa': encuesta_activa})
      return context

class VotarEncuestaView(TemplateView):
    template_name = "weblog/encuesta_gracias.html"
    
    def get(self, request, *args, **kwargs):
      encuestas_activas = Encuesta.objects.filter(activa=True).order_by('fecha_publicacion')
      if encuestas_activas:
          encuesta_activa = encuestas_activas[0]
          opcion = encuesta_activa.opcionencuesta_set.filter(id=request.GET['opcion'])[0]
          opcion.votos += 1
          opcion.save()
      return render_to_response("weblog/encuesta_gracias.html")

class ArtistasView(TemplateView):
	template_name = "weblog/artistas.html"

	def get_context_data(self):
		context = super(ArtistasView, self).get_context_data()
		letra = self.request.GET.get('letra')
		artistas = Artista.objects.filter(nombre__startswith=letra)
		paginator = Paginator(artistas, 10)
		page = self.request.GET.get('page')
		try:
			artistas = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			artistas = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			artistas = paginator.page(paginator.num_pages)
		context.update({'artistas': artistas, 'page_obj': artistas})
		return context


def index(request):
	last_news = Entry.objects.all()[:1]
	artists = Artista.objects.all()[:4]
	context = {'last_news': last_news, 'artists': artists}
	return render(request, 'weblog/index.html', context)
