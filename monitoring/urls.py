"""IoTransit_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^sensores/ver/(?P<pk>\d+)/$', csrf_exempt(views.voy), name='voy'),
    url('^sensores/predicciones', csrf_exempt(views.redNeuronal), name='redNeuronal'),
    url('^sensores/$', csrf_exempt(views.sensores), name='sensores'),
    url('^video/$', csrf_exempt(views.emopy), name='emopy'),

    url(r'^$', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
