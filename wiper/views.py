from django.shortcuts import render
from .models import Document, Publication


# Create your views here.

def index(request):
    documents = Document.objects.all()
    publications = Publication.objects.all()
    context = {'documents': documents, 'publications': publications}
    return render(request, 'index.html', context)


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
