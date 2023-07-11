from django.contrib import admin
from django.urls import path, re_path
from cakes.views import *
from markets.views import *
from accounts.views import *

from rest_framework import routers
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

import re

routers = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title = "cakekku-project",
        default_version = "v1",
        description = "cakekku api문서입니다. 이거 구현하는데 12시간 넘게 걸렸으니 유용하게 써주세요 :)",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('marketlist/', MarketListAPIView.as_view()),
    path('marketdetail/<int:pk>/', MarketRetrieveAPIView.as_view()),
    path('createreview/', ReviewCreateAPIView.as_view()),
    path('createcake/', CakeCreateAPIView.as_view()),
    path('myreviewlist/', MyReviewList.as_view()),
    path('logintempuser/', LoginTempUser.as_view()),
    path('marketlike/',MarketLike.as_view()),
    path('market/',MarketList.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

