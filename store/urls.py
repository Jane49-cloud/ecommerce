"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, re_path
from product import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.index),
    re_path(r'^$', views.index, name='home'),
    re_path(r'^categories/(?P<pk>\d+)/$', views.category_products, name='category_products'),
    re_path(r'^products/(?P<pk>\d+)/$', views.single_product, name='single_product'),
    re_path(r'^admin/', admin.site.urls),
     re_path(r'^signin/', views.SignUpView.as_view(), name='signin'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
