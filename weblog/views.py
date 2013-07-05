from django.shortcuts import render, get_object_or_404
from weblog.models import Encuesta, OpcionEncuesta
from django.views.generic import TemplateView

class EncuestaActivaView(TemplateView):
    template_name = "weblog/encuesta_activa.html"
    
    def get_context_data(self):
      context = super(EncuestaActivaView, self).get_context_data()
      encuesta_activa = Encuesta.objects.filter(activa=True).order_by('fecha_publicacion')[0]
      opciones_encuesta = OpcionEncuesta.objects.filter(encuesta=encuesta_activa)
      context.update({'opciones_encuesta' : opciones_encuesta, 'encuesta_activa': encuesta_activa})
      return context


