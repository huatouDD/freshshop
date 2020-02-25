from rest_framework import serializers

# class GoodsSerializer(serializers.Serializer):
#     """
#     goods的序列化器
#     """
#
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    """
    # category 为goods的外键, 显示的时候只有id, 这时想嵌套展示,需要创建分类Category的序列化器
    """

    class Meta:
        """
        三级分类
        """
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    """
    二级分类
    """
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    一级分类
    """
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    """
    inherit ModelSerializer
    """

    # category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
