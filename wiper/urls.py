from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about_us, name='about-us'),
    path('party-documents/', views.party_documents, name='party-documents'),
    path('notices/', views.notices, name='notices'),
    path('careers/', views.careers, name='careers'),
    path('tenders/', views.tenders, name='tenders'),
    path('financial-statements/', views.financial_statements, name='financial-statements'),
    path('leadership/', views.leadership, name='leadership'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
    
]
