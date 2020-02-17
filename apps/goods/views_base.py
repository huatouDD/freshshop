from django.forms.models import model_to_dict
import json

from django.http import JsonResponse
from django.views.generic.base import View

from goods.models import Goods


# 使用类视图传统方法进行数据返回
class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()
        """
        第一种： 直接数据组装返回
                # for good in goods:
                    # json_dict = {}
                    # json_dict['name'] = good.name
                    # json_dict['category'] = good.category.name
                    # json_dict['market_price'] = good.market_price
        """
        """
        第二种： 利用django.forms.model中的model_to_dict方法进行数据format.缺点： 有些字段不能to_dict（如，ImageField）
        
                # 使用django的model_to_dict
                # json_dict = model_to_dict(good)
                # json_list.append(json_dict)
        
        """
        """
        第三种： 直接利用django的核心core中的序列化器serializers.serialize进行数据的序列化 （将数据变为json数据）
        """
        from django.core.serializers import serialize
        json_data = serialize('json', goods)
        print(type(json_data), json_data)
        json_data = json.loads(json_data)

        from django.http import HttpResponse
        # return HttpResponse(json.dumps(json_list), content_type='application/json')
        return JsonResponse(json_data, safe=False)
