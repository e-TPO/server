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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
<<<<<<< HEAD
    url(r'^', include('placement.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    url(r'^notice/', include('notice.urls')),
]
>>>>>>> bb1e6b57eb9a3aa1c2e8a0390db8c1c8e6906d4f

admin.site.site_header = 'e-TPO Admin Panel'
admin.site.site_title = 'e-TPO Admin Panel'