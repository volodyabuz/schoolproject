from django.contrib import admin
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index, name='home'),
    path('all', cache_page(60)(AllPosts.as_view()), name='all'),
    path('register', Register.as_view(), name='register')
]
