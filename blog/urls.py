from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('trading/', views.trading, name='blog-trading'),
    path('about/', views.about, name='blog-about'),
]
