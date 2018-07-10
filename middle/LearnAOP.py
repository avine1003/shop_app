# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

__author__ = "wuyou"
__date__ = "2018/7/10 19:33"

import random
import time


class HelloMiddle(MiddlewareMixin):
    def process_request(self, request):
        print(request.path)
        print(request.META.get('REMOTE_ADDR'))

        # 黑白名单简单案例
        if request.path == '/axf/getphone/':
            if request.META.get('REMOTE_ADDR') == '192.168.51.66':
                num = random.randrange(100)
                if num > 50:
                    return HttpResponse('特殊手段抽到手机')

        ip = request.META.get('REMOTE_ADDR')
        black = cache.get('black', [])
        if ip in black:
            return HttpResponse('请求过于频繁，请稍后再试')

        # if request.path == '/axf/getphone/':
        #     result = cache.get(ip)
        #     if result:
        #         return HttpResponse('每10秒只能访问一次')
        #     else:
        #         cache.set(ip, 'BLACK', 10)

        # 基于请求频率的反爬
        history = cache.get(ip, [])
        # history不为空， 获取最后一个元素和请求时间，与当前时间比较，超过60弹出
        while history and history[-1] <= time.time() - 60:
            history.pop()
        if len(history) <= 10:
            history.insert(0, time.time())
            cache.set(ip, history, 60)
        else:
            return HttpResponse('请求异常')


