from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from . import host
from .. import db
from ..models import Permission, Role, User, Post, Comment
from ..decorators import admin_required, permission_required
from ..bwlist import mysqldb
from . import socketcheck
import json


###域名部分########################

#页面
@host.route('/host',methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def host1():
    return render_template('host/hostcheck.html')
#检测所有
@host.route('/host/<port>', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def host2(port):
    hostall=str(socketcheck.check.scan(int(port)))
    return hostall
#检测单个
@host.route('/checkhost/<host>', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def host3(host):
    a=socketcheck.check.hostportcheck(str(host))
    return str(a)
#端口排查类
@host.route('/scan', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def scan():
    return render_template('host/scan.html')
#端口排查返回数据
@host.route('/scan/<host>/<port>', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def scan1(host,port):
    a=socketcheck.check.hostportcheckint(str(host),int(port))
    return a
    # return render_template('host/hostcheck.html',a=a,b=b)