import json

import requests

class YunPian(object):
    """
    云片验证码
    """

    def __init__(self, api_key):
        self.api_key = api_key  # key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        """
        发送短信
        :param code:
        :param mobile:
        :return:
        """
        # 设置需要的参数
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【jayyywah's home】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        return re_dict
