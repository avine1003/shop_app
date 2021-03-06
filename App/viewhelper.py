# -*- coding: utf-8 -*-
__author__ = "wuyou"
__date__ = "2018/7/5 10:06"

from App.models import UserModel, Cart


def get_user(username):
    try:
        user = UserModel.objects.get(u_name=username)
        return user
    except:
        return None


# def send_mail_to(username, active_url, receive_mail):
#     subject = '欢迎入坑'
#     temp = loader.get_template('user/user_active.html')
#
#     data = {
#         'username': username,
#         'active_url': active_url,
#     }
#     html_message = temp.render(context=data)
#
#     send_mail(subject,'', from_email="wusezdhwuyou@163.com", recipient_list=[receive_mail],
#               html_message=html_message)


def get_user_by_id(user_id):
    try:
        user=UserModel.objects.get(pk=user_id)
        return user
    except:
        return None


def get_total_price(user_id):
    carts = Cart.objects.filter(c_user_id=user_id)

    total_price = 0

    for cart_obj in carts:
        if cart_obj.is_select:
            total_price += cart_obj.c_goods_num * cart_obj.c_goods.price
    return total_price

