from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import *


# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-created_at')[:3]

    context = {
        'posts': posts,
        'nav': 'index',
    }
    return render(request, 'index.html', context)


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def news(request):
    posts_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 6)  # Show 6 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'nav': 'news',
        'posts': posts,
    }
    return render(request, 'news.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    recent_posts = Post.objects.all().order_by('-created_at').exclude(id=post.id).distinct()[:3]

    context = {
        'post': post,
        'categories': categories,
        'recent_posts': recent_posts,
    }

    return render(request, 'post-detail.html', context)


def contact(request):
    context = {'nav': 'contact', }
    return render(request, 'contact.html', context)


def about_us(request):
    context = {}
    return render(request, 'about-us.html', context)


def notices(request):
    party_notices = PDFDocument.objects.filter(category__name="Tenders")
    context = {'notices': party_notices}
    return render(request, 'notices.html', context)


def careers(request):
    jobs = PDFDocument.objects.filter(category__name="Careers")
    context = {'jobs': jobs}
    return render(request, 'careers.html', context)


def tenders(request):
    open_tenders = PDFDocument.objects.filter(category__name="Tenders")
    context = {'tenders': open_tenders}
    return render(request, 'tenders.html', context)


def financial_statements(request):
    finance_statements = PDFDocument.objects.filter(category__name="Financial Statements")
    context = {'finance_statements': finance_statements}
    return render(request, 'financial-statements.html', context)


def party_documents(request):
    pdfdocs = PDFDocument.objects.filter(category__name="Party Documents")
    context = {'pdfdocs': pdfdocs}
    return render(request, 'party-documents.html', context)


def leadership(request):
    leaders = PDFDocument.objects.filter(category__name="Leadership")

    context = {'leaders': leaders}
    return render(request, 'leadership.html', context)
