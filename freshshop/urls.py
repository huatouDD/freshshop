"""freshshop URL Configuration

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
# from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from freshshop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet
from apps.users.views import SmsCodeViewSet

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet)
router.register(r'categorys', CategoryViewSet, basename='categorys')
router.register(r'verifyCode', SmsCodeViewSet, basename='verify_code')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # path('goods/', GoodsListView.as_view(), name='goods-list'),
    path('docs', include_docs_urls(title='钢仔')),
    path('api-auth', include('rest_framework.urls')),
    # 首页展示drf的相关api
    re_path('^', include(router.urls)),
    # drf-token
    path('api-token-auth/', views.obtain_auth_token),

    # drf-jwt
    path('login/', obtain_jwt_token)
]
