from django.shortcuts import render
from .models import Document, Publication


# Create your views here.

def index(request):
    documents = Document.objects.all()
    publications = Publication.objects.all()
    context = {'documents': documents, 'publications': publications, 'nav': 'index'}
    return render(request, 'index.html', context)


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def news(request):
    context={'nav': 'news'}
    return render(request, 'news.html', context)


def contact(request):
    context={'nav': 'contact'}
    return render(request, 'contact.html', context)

def about_us(request):
    context={}
    return render(request, 'about-us.html', context)


def downloads(request):
    context={}
    return render(request, 'downloads.html')

def notices(request):
    context={}
    return render(request, 'notices.html', context)

def careers(request):
    context={}
    return render(request, 'careers.html', context)

def tenders(request):
    context={}
    return render(request, 'tenders.html', context)

def financial_statements(request):
    context={}
    return render(request, 'financial-statements.html', context)