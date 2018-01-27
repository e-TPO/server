"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from placement import views as placement_views
from auth import views as auth_views

handler404 = 'auth_views.handler404'
handler500 = 'auth_views.handler500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    # url(r'^notice/', include('notice.urls')),
    url(r'^placement/', include('placement.urls')),
    url(r'^login', auth_views.login_view),
    url(r'^logout', auth_views.logout_view),
    url(r'^signup', auth_views.signup_view),
    url(r'^$', placement_views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'e-TPO Admin Panel'
admin.site.site_title = 'e-TPO Admin Panel'