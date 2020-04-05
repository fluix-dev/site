from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
