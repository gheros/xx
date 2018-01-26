from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from . import bwlist
from .. import db
from ..models import Permission, Role, User, Post, Comment
from ..decorators import admin_required, permission_required
from . import bwlist
from . import readfile
from . import mysqldb
import json
from .black import user_client,blacklist,whitelist
@bwlist.route('/index', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def index():
    c = user_client('xx')
    c1 = blacklist('hm')
    print(type(c.scan()))
    c2 = json.dumps(c.scan())
    return render_template('bwlist/index.html',cname=c.scan())

@bwlist.route('/blist/<lname>')
@login_required
@permission_required(Permission.BWLISTIP)
def blist(lname):
    c1 =blacklist(lname)
    c2=str(c1.scan())
    return c2
#增加黑名单
@bwlist.route('/addblist/<lname>/<ipadd>')
@login_required
@permission_required(Permission.BWLISTIP)
def blistadd(lname,ipadd):
    ipadd=ipadd.strip()
    c1 = blacklist(lname)
    rc= c1.insert(ipadd)
    c2=str(rc)
    return c2
#删除黑名单
# @bwlist.route('/delblist/<rname>/<ipdel>',methods=['GET'])
# @login_required
# @permission_required(Permission.BWLISTIP)
# def blistdel(rname,ipdel):
#     c1 = blacklist(rname)
#     rc= c1.delete(ipdel)
#     return rc
#查看白名单
@bwlist.route('/wlist/<wname>')
@login_required
@permission_required(Permission.BWLISTIP)
def wlist(wname):
    c1 =whitelist(wname)
    c2=str(c1.scan())

    return c2

#增加白名单
@bwlist.route('/addwlist/<wname>/<wipadd>')
@login_required
@permission_required(Permission.BWLISTIP)
def wlistadd(wname,wipadd):
    wipadd=wipadd.strip()
    c1 = whitelist(wname)
    rc= c1.insert(wipadd)
    c2=str(rc)
    return c2
#批量增加白名单
# @bwlist.route('/addwlist/<wname>',methods=['POST'])
# @login_required
# @permission_required(Permission.BWLISTIP)
# def wlistadd(wname):
#     wipadd=wipadd.strip()
#     c1 = whitelist(wname)
#     rc= c1.insert(wipadd)
#     c2=str(rc)
#     return c2

# #删除白名单
# @bwlist.route('/delwlist/<wname>/<wipdel>',methods=['GET'])
# @login_required
# @permission_required(Permission.BWLISTIP)
# def wlistdel(wname,wipdel):
#     c1 = whitelist(wname)
#     rc= c1.delete(wipdel)
#     return rc
#更新提交动作
@bwlist.route('/submit/<name>',methods=['GET'])
@login_required
@permission_required(Permission.BWLISTIP)
def submit(name):

    return

@bwlist.route('/doc/<name>',methods=['GET'])
@login_required
@permission_required(Permission.BWLISTIP)
def doc(name):
    if name=="about":
        return render_template('about.html')



###域名部分########################
# #
# #域名页面
# @bwlist.route('/domain',methods=['GET'])
# @login_required
# @permission_required(Permission.BWLISTIP)
# def domain():
#     scan=json.dumps(dm.domain.scan())
#     return render_template('domain/domain.html',cname=scan)
# #添加域名
# @bwlist.route('/doinsert/<name>/<domainn>',methods=['GET'])
# @login_required
# @permission_required(Permission.BWLISTIP)
# def doinsert(name,domainn):
#     if name=="about":
#         return
# #删除域名
# @bwlist.route('/dodelete/<name>/<domainn>',methods=['GET'])
# @login_required
# @permission_required(Permission.BWLISTIP)
# def dodelete(name,domainn):
#     if name=="about":
#         return
# #查询域名
# @bwlist.route('/dosearch/<name>/<domainn>',methods=['GET'])
# @login_required
# @permission_required(Permission.BWLISTIP)
# def dosearch(name,domainn):
#     if name=="about":
#         return
# @bwlist.route('/docat/<name>',methods=['GET'])
# @login_required
# @permission_required(Permission.BWLISTIP)
# def docat(name):
#     docat=dm.domain(name).docat()
#     return docat


