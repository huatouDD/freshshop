# 独立的使用django的model

import sys
import os

# 获取当前文件的路径（运行脚本）
pwd = os.path.dirname(os.path.realpath(__file__))

# 获取项目的根目录
sys.path.append(pwd + "../")

# 参照manage.py, 单独使用django的model,需要指定一个环境变量, 会去setting中找
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freshshop.settings")

import django

django.setup()

from goods.models import GoodsCategory
from db_tools.data.category_data import row_data

# 一级类
for lev1_cat in row_data:
    lev1_instance = GoodsCategory()
    lev1_instance.code = lev1_cat["code"]
    lev1_instance.name = lev1_cat["name"]
    lev1_instance.category_type = 1
    # save data
    lev1_instance.save()
    # 二级类
    for lev2_cat in lev1_cat['sub_categorys']:
        lev2_instance = GoodsCategory()
        lev2_instance.code = lev2_cat['code']
        lev2_instance.name = lev2_cat['name']
        lev2_instance.category_type = 2
        lev2_instance.parent_category = lev1_instance
        # save data
        lev2_instance.save()

        # 三级类
        for lev3_cat in lev2_cat['sub_categorys']:
            lev3_instance = GoodsCategory()
            lev3_instance.code = lev2_cat['code']
            lev3_instance.name = lev2_cat['name']
            lev3_instance.category_type = 3
            lev3_instance.parent_category = lev2_instance
            # save data
            lev3_instance.save()
