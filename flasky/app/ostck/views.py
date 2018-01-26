from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from . import ostck

from ..models import Permission, Role, User, Post, Comment
from ..decorators import admin_required, permission_required



###域名部分########################

#页面
@ostck.route('/ostck',methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def ostckindex():
    return render_template('ostck/index.html')
#
@ostck.route('/ostck/<param>',methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def costck(param):
    print(param)

    print(type(param))

    x = param.split('&')

    print(x)

    # x = '22222222&&&1'
    # b = x.split('&')
    # print(b)
    return 'xx'
#检测所有
# @ostck.route('/ostck/22',methods=['GET', 'POST'])
# def ostck1():
#     return ''
# @ostck.route('/ostck/<lname>')
# @login_required
# @permission_required(Permission.BWLISTIP)
# def ostck2(lname):
#     return lname

def check(ip,type,wip,disk):
    print(ip)
    print(type)
    print(wip)
    print(disk)
