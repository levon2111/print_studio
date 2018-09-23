"""print_studio URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.static import serve
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from apps.order.views import HolderTypeViewSet, OrderModelViewSet

schema_view = get_swagger_view(title='Print Studio API')
router = routers.DefaultRouter()
router.register(r'holder-type', HolderTypeViewSet, base_name='holder-type')
router.register(r'order', OrderModelViewSet, base_name='order')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls'))

]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
