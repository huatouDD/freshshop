from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Goods
from goods.serializers import GoodsSerializer


class GoodsListView(APIView):
    """
    商品列表
    """
    def get(self, request):
        goods = Goods.objects.all()
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)