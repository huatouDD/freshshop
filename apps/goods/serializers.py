from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    """
    goods的序列化器
    """

    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()
