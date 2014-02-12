from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage
from weblog.models import Entry, Artista


def search(request):
    query = request.GET.get('q', '')
    filtro = request.GET.get('tipo', '')
    results = []
    if query:
    	if filtro == "artistas":
    		results = list(Artista.objects.filter(nombre__icontains=query))
    	elif filtro == "noticias":
    		results = list(Entry.objects.filter(title__icontains=query))
    	else:
    		res1 = list(Entry.objects.filter(title__icontains=query))
        	res2 = list(Artista.objects.filter(nombre__icontains=query))
    		results = res1 + res2
    else:
    	results = []

    return render(request, 'search/search.html', {'query': query,
                                                  'results': results
                                                  })
