"""telusko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import re_path
from django.views.static import serve
from django.urls import path
from payment import views

urlpatterns = [
    path('', include('travello.urls')),
    path('admin/', admin.site.urls),
    path("payment/", include('payment.urls')),
    path('accounts/', include('accounts.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),    
]

# Will work only in Development mode and not in Deployment Mode as Django does not handle Static Files. We use WhiteNoise to handle static files of Django
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 