# -*- coding: utf-8 -*-
__author__ = "wuyou"
__date__ = "2018/7/5 10:06"

from django.core.mail import send_mail
from django.template import loader

from App.models import UserModel


def get_user(username):
    try:
        user = UserModel.objects.get(u_name=username)
        return user
    except:
        return None


def send_mail_to(username, active_url, receive_mail):
    subject = '欢迎入坑'
    temp = loader.get_template('user/user_active.html')

    data = {
        'username': username,
        'active_url': active_url,
    }
    html_message = temp.render(context=data)

    send_mail(subject,'', from_email="wusezdhwuyou@163.com", recipient_list=[receive_mail],
              html_message=html_message)
