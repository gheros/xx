from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from . import domain
from .. import db
from ..models import Permission, Role, User, Post, Comment
from ..decorators import admin_required, permission_required
from ..bwlist import mysqldb
from . import domainc
import json


###域名部分########################

#域名页面
@domain.route('/domain',methods=['GET', 'POST'])
@login_required
@permission_required(Permission.BWLISTIP)
def domain1():
    scan=json.dumps(domainc.domain.scan())
    return render_template('domain/domain.html',cname=scan)
#添加域名
@domain.route('/doinsert/<name>/<domainn>',methods=['GET'])
def doinsert(name,domainn):
    domainn = domainn.strip()
    a=domainc.domain(name).insert(domainn)
    return a
# #删除域名
@domain.route('/dodelete/<name>/<domainn>',methods=['GET'])
@login_required
@permission_required(Permission.BWLISTIP)
def dodelete(name,domainn):
    domainn = domainn.strip()
    a = domainc.domain(name).delete(domainn)
    return a
# #检查域名
@domain.route('/docheck/<name>/<domainn>',methods=['GET'])
@login_required
@permission_required(Permission.BWLISTIP)
def docheck(name,domainn):
    domainn=domainn.strip()
    a = domainc.domain(name).check(domainn)
    return a
@domain.route('/docat/<name>',methods=['GET'])
@login_required
@permission_required(Permission.BWLISTIP)
def docat(name):
    docat=str(domainc.domain(name).docat())
    return docat
