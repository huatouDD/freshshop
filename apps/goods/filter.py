import django_filters

from goods.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤的类
    """
    price_max = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    price_min = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte')

    class Meta:
        model = Goods
        fields = [
            'price_min', 'price_max'
        ]