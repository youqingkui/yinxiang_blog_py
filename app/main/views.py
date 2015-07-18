#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from . import main
from app.models import User
from evernote.api.client import EvernoteClient

@main.route('/', methods=['GET', 'POST'])
def index():
    u = User()
    u.email = "youqingkui@qq.com"
    u.first_name = "youqing"
    u.last_name = "kui"
    u.save()
    return  "ok"


@main.route('/yx')
def yx():
    """
    测试印象笔记服务
    :return:
    """
    client = EvernoteClient(token=dev_token,sandbox=False)
    client.service_host = 'app.yinxiang.com'
    userStore = client.get_user_store()
    user = userStore.getUser()
    print user
    return "yx"
