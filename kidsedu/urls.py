from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('all', AllPosts.as_view(), name='all'),
    # path('register', Register.as_view(), name='register')
]
