from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Goods
from goods.serializers import GoodsSerializer
from rest_framework import generics


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


class GoodsListView(generics.ListAPIView):
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
