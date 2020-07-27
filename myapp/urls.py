from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('feed/rss/', views.RSSBlogFeed(), name='rss-feed'),
    path('feed/atom/', views.AtomBlogFeed(), name='atom-feed'),
    path('<slug:slug>', views.BlogView.as_view(), name='blog'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
]
