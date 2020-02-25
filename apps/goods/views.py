from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.filter import GoodsFilter
from goods.models import Goods, GoodsCategory
from goods.serializers import GoodsSerializer, CategorySerializer
from rest_framework import generics, mixins, viewsets, filters


# class GoodsListView(APIView):
#     """
#     商品列表
#     """
#     def get(self, request):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)
class GoodsPagination(PageNumberPagination):
    """
    商品自定义分页
    """
    # 每页展示的数量
    page_size = 15
    # 利用url上的参数-->> 动态的改变每页展示的数量
    page_size_query_param = 'page_size'
    # 输出在url上的参数
    page_query_param = 'page'
    # 最多多少页
    max_page_size = 100


# class GoodsListView(generics.ListAPIView):
#     pagination_class = GoodsPagination
#     serializer_class = GoodsSerializer
#     queryset = Goods.objects.all()

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    # 必须带排序，不然报错
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # 自定义过滤器
    filter_class = GoodsFilter

    search_fields = ('=name', 'goods_brief')
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    分类列表
    """
    serializer_class = CategorySerializer
    queryset = GoodsCategory.objects.filter(category_type=1)