from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage
from weblog.models import Entry


def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Entry.objects.filter(title__icontains=query)
    return render(request, 'search/search.html', {'query': query,
                                                  'results': results
                                                  })
