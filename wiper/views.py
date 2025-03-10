from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *


# Create your views here.

def index(request):
    documents = Document.objects.all()
    publications = Publication.objects.all()
    context = {'documents': documents, 'publications': publications, 'nav': 'index'}
    return render(request, 'index.html', context)


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def news(request):
    posts_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 6)  # Show 6 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context={'nav': 'news', 'posts': posts}
    return render(request, 'news.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post-detail.html', {'post': post})

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