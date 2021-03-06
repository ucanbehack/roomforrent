"""roomfrent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
#    path('admin/', admin.site.urls),
    url(r'', include('search.urls')),
    url(r'^siteadmin/', admin.site.urls),
    url(r'^dashboard/', include('search.urls')),
    url(r'^owner/',include('owner.urls')),
    url(r'^scrap/',include('scrap.urls')),
    url(r'^favicon.ico$',
        RedirectView.as_view( # the redirecting function
            url=staticfiles_storage.url('images/fevi_icon_logo.ico'), # converts the static directory + our favicon into a URL
            # in my case, the result would be http://www.tumblingprogrammer.com/static/img/favicon.ico
        ),
        name="favicon" # name of our view
    ),
]
