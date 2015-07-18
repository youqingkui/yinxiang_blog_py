#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from . import main
from app.models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    u = User()
    u.email = "youqingkui@qq.com"
    u.first_name = "youqing"
    u.last_name = "kui"
    u.save()
    return  "ok"