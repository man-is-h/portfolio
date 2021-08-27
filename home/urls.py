from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Developer Manish"
admin.site.site_title = "Welcome to my Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('projects/', views.projects, name = 'projects'),
    path('contact/', views.contact, name = 'contact'),
    path('about/intro/', views.intro, name = 'introduction'),
    path('about/edu/', views.edu, name = 'education'),
    path('about/exp/', views.exp, name = 'experience'),    
]