#
#   ____         __  __                  _
#  |  _ \       / _|/ _|     /\         (_)
#  | |_) |_   _| |_| |_     /  \   _ __  _
#  |  _ <| | | |  _|  _|   / /\ \ | '_ \| |
#  | |_) | |_| | | | |    / ____ \| |_) | |
#  |____/ \__,_|_| |_|   /_/    \_\ .__/|_|
#                                 | |
#                                 |_|
# Buff-Api By jiajiaxd(https://github.com/jiajiaxd)
# 请在遵守GPL-3.0协议的前提下使用本API。
# 仅供学习交流使用，所造成的一切后果将由使用者自行承担！

import json
import time
from typing import List

import requests
import random
import copy


def get_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


def get_random_header() -> dict:
    return {'User-Agent': get_ua()}


class BuffAccount:
    """
    支持自定义User-Agent
    参数为Buff的cookie
    参考格式：
    session=*******
    若报错，大概率是因为你被BUFF的反爬虫机制检测到了，请多次尝试！

    附：
    Buff的每个商品的每种磨损（品质）均有一个独立的goods_id,每一件商品都有一个独立的id
    """

    def __init__(self, buffcookie, user_agent=get_ua()):
        self.session = requests.session()
        self.session.headers = {'User-Agent': user_agent}
        headers = copy.deepcopy(self.session.headers)
        headers['Cookie'] = buffcookie
        try:
            self.username = json.loads(
                self.session.get('https://buff.163.com/account/api/user/info', headers=headers).text).get('data').get(
                'nickname')
        except AttributeError:
            raise ValueError('Buff登录失败！请稍后再试或检查cookie填写是否正确.')

    def get_user_nickname(self) -> str:
        """
        :return: str
        """
        return self.username

    def get_user_brief_assest(self) -> dict:
        """
        包含用户余额等信息
        :return: dict
        """
        return json.loads(
            self.session.get('https://buff.163.com/api/asset/get_brief_asset').text).get('data')

    def search_goods(self, key: str, game_name='csgo') -> list:
        return json.loads(self.session.get('https://buff.163.com/api/market/search/suggest', params={
            'text': key,
            'game': game_name
        }).text).get('data').get('suggestions')

    def get_sell_order(self, goods_id, page_num=1, game_name='csgo', sort_by='default', proxy=None) -> dict:
        """
        获取指定饰品的在售商品
        :return: dict
        """
        params = {'game': game_name,
                  'goods_id': goods_id,
                  'page_num': page_num,
                  'sort_by': sort_by}
        if sort_by != 'default':
            return json.loads(self.session.get('https://buff.163.com/api/market/goods/sell_order', params=params,
                                               headers=get_random_header(), proxies=proxy).text).get('data')
        else:
            return json.loads(requests.get('https://buff.163.com/api/market/goods/sell_order', params=params,
                                           headers=get_random_header(), proxies=proxy).text).get('data')

    def get_available_payment_methods(self, sell_order_id, goods_id, price, game_name='csgo') -> dict:
        """
        :param game_name:默认为csgo
        :param sell_order_id:
        :param goods_id:
        :param price:饰品价格
        :return: dict key只会包含buff-alipay和buff-bankcard，若不存在key，则代表此支付方式不可用。value值为当前余额
        """

        methods = json.loads(self.session.get('https://buff.163.com/api/market/goods/buy/preview', params={
            'game': game_name,
            'sell_order_id': sell_order_id,
            'goods_id': goods_id,
            'price': price
        }).text).get('data').get('pay_methods')
        available_methods = dict()
        if methods[0].get('error') is None:
            available_methods['buff-alipay'] = methods[0].get('balance')
        if methods[2].get('error') is None:
            available_methods['buff-bankcard'] = methods[2].get('balance')
        return available_methods

    def buy_goods(self, sell_order_id, goods_id, price, pay_method: str, ask_seller_send_offer: bool,
                  game_name='csgo'):
        """
        由于部分卖家禁用了由卖家发起报价，因此不推荐使用此API
        :param sell_order_id:
        :param goods_id:
        :param price:
        :param pay_method:仅支持buff-alipay或buff-bankcard.
        :param ask_seller_send_offer: 是否要求卖家发送报价
        若为False则为由买家发送报价
        警告：本API并不会自动发起报价，报价需要用户在手机版BUFF上发起！！！
        若卖家禁用了由卖家发起报价，则会自动更改为由买家发送报价！！！
        建议与github.com/jiajiaxd/Buff-Bot配合使用，效果更佳！
        :param game_name: 默认为csgo
        :return:若购买成功则返回'购买成功'，购买失败则返回错误信息
        """
        load = {
            'game': game_name,
            'goods_id': goods_id,
            'price': price,
            'sell_order_id': sell_order_id,
            'token': '',
            'cdkey_id': ''
        }
        if pay_method == 'buff-bankcard':
            load['pay_method'] = 1
        elif pay_method == 'buff-alipay':
            load['pay_method'] = 3
        else:
            raise ValueError('Invalid pay_method')
        headers = copy.deepcopy(self.session.headers)
        headers['accept'] = 'application/json, text/javascript, */*; q=0.01'
        headers['content-type'] = 'application/json'
        headers['dnt'] = '1'
        headers['origin'] = 'https://buff.163.com'
        headers['referer'] = 'https://buff.163.com/goods/' + str(goods_id) + '?from=market'
        headers['x-requested-with'] = 'XMLHttpRequest'
        # 获取最新csrf_token
        self.session.get('https://buff.163.com/api/message/notification')
        self.session.cookies.get('csrf_token')
        headers['x-csrftoken'] = self.session.cookies.get('csrf_token')
        response = json.loads(
            self.session.post('https://buff.163.com/api/market/goods/buy', json=load, headers=headers).text)
        bill_id = response.get('data').get('id')
        self.session.get('https://buff.163.com/api/market/bill_order/batch/info', params={'bill_orders': bill_id})
        headers['x-csrftoken'] = self.session.cookies.get('csrf_token')
        time.sleep(0.5)  # 由于Buff服务器处理支付需要一定的时间，所以一定要在这里加上sleep，否则无法发送下一步请求
        if ask_seller_send_offer:
            load = {
                'bill_orders': [bill_id],
                'game': game_name
            }
            response = self.session.post('https://buff.163.com/api/market/bill_order/ask_seller_to_send_offer',
                                         json=load, headers=headers)
        else:
            load = {
                'bill_order_id': bill_id,
                'game': game_name
            }
            response = self.session.post('https://buff.163.com/api/market/bill_order/notify_buyer_to_send_offer',
                                         json=load, headers=headers)
        response = json.loads(response.text)
        if response.get('msg') is None and response.get('code') == 'OK':
            return "购买成功"
        else:
            return response

    def get_notification(self) -> dict:
        """
        获取notification
        :return: dict
        """
        return json.loads(self.session.get("https://buff.163.com/api/message/notification").text).get('data')

    def get_steam_trade(self) -> dict:
        return json.loads(self.session.get("https://buff.163.com/api/market/steam_trade").text).get('data')

    def get_items(self, goods_id, include_sticker, min_price = 0, game_name='csgo') -> dict:
        """查询饰品在售最低价格。
            可用服务：开发者API 或 企业API
            查询范围：全站饰品
            更新频率：include_sticker为0时，5分钟/次；include_sticker为1时，10分钟/次
            请求次数：10000次/月
            备注：goods_id 非必需，若不指定，则1次请求返回全站有在售的饰品价格，约2万饰品。
        Args:
            min_price (number): 在售价格过滤参数，非必需。
            goods_id (string): 指定单个饰品ID，非必需。
            include_sticker (integer): 仅在未指定 goods_id 时生效，include_sticker 为 0 时，返回结果不含涂鸦，印花与印花板饰品，数据更实时。
            game_name (str): 游戏ID，必需。

        Returns:
            dict: _description_
        """
        parameters = {
            'game': game_name,
            'goods_id': goods_id,
            'min_price': min_price,
            'include_sticker': include_sticker
        }
        return json.loads(requests.get('https://buff.163.com/api/market/items', params=parameters,).text).get('info')
    
    def get_items(self, goods_ids : List[int], min_price = 0) -> dict:
        """查询饰品磨损区间最低价格、渐变度区间最低价格、磨损区间在售数量、饰品流通性百分比。
            可用服务：开发者API 或 企业API
            查询范围：全站饰品，每日最多查询其中200个饰品，当日已查询的可重复查询。
            更新频率：饰品流通性1天/次，其余数据10分钟/次
            请求次数：10000次/月
            备注：
            goods_id 为必需，不能为空。
            饰品流通性：大比例成交金额排名与小比例成交量排名加权计算，通常认为≥85%饰品较热门。

        Args:
            goods_ids (_type_): 饰品id列表，必需。
            min_price (int, optional): _description_. Defaults to 0.

        Returns:
            dict: _description_
        """
        parameters = {
            'goods_ids': goods_ids,
            'min_price': min_price,
        }
        return json.loads(requests.post('https://buff.163.com/api/market/float/items', json=parameters,).text).get('info')