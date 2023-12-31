"""
URL configuration for schooledu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG, STATIC_URL, STATIC_ROOT
from kidsedu.views import view_404
from django.views.static import serve as mediaserve
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kidsedu.urls')),
    path('captcha/', include('captcha.urls')),
]

if DEBUG:
    urlpatterns = [path("__debug__/", include("debug_toolbar.urls")),] + urlpatterns
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
# else:
#     urlpatterns += [
#         url(f'^{MEDIA_URL.lstrip("/")}(?P<path>.*)$',
#             mediaserve, {'document_root': MEDIA_ROOT}),
#         url(f'^{STATIC_URL.lstrip("/")}(?P<path>.*)$',
#             mediaserve, {'document_root': STATIC_ROOT}),
#     ]

handler404 = view_404
