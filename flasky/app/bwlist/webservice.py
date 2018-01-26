
import json
from flask import Flask, session, redirect, url_for, escape, request,render_template
from model.black import user_client,blacklist,whitelist


app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')

    return render_template('base.html' )

@app.route('/black', methods=['GET', 'POST'])
@app.route('/black/<name>', methods=['GET', 'POST'])
@app.route('/black/<name>/<blackl>', methods=['GET', 'POST'])
def login(name=None,blackl=None):
    print(name)
    print(blackl)
    c=user_client('xx')
    c1=blacklist('hm')
    print(type(c.scan()))
    c2=json.dumps(c.scan())
    return render_template('bwlist.html',cname=c.scan())
@app.route('/blist/<lname>')
def blist(lname):

    c1 =blacklist(lname)
    c2=str(c1.scan())

    return c2
#增加黑名单
@app.route('/addblist/<lname>/<ipadd>')
def blistadd(lname,ipadd):
    c1 = blacklist(lname)
    rc= c1.insert(ipadd)
    return rc
#删除黑名单
@app.route('/delblist/<rname>/<ipdel>',methods=['GET'])
def blistdel(rname,ipdel):
    c1 = blacklist(rname)
    rc= c1.delete(ipdel)
    return rc
#查看白名单
@app.route('/wlist/<wname>')
def wlist(wname):
    c1 =whitelist(wname)
    c2=str(c1.scan())

    return c2

#增加白名单
@app.route('/addwlist/<wname>/<wipadd>')
def wlistadd(wname,wipadd):
    c1 = whitelist(wname)
    rc= c1.insert(wipadd)
    return rc
#删除白名单
@app.route('/delwlist/<wname>/<wipdel>',methods=['GET'])
def wlistdel(wname,wipdel):
    c1 = whitelist(wname)
    rc= c1.delete(wipdel)
    return rc
#更新提交动作
@app.route('/submit/<name>',methods=['GET'])
def submit(name):

    return

@app.route('/doc/<name>',methods=['GET'])
def doc(name):
    if name=="about":
        return render_template('about.html')

    return


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run('0.0.0.0','8866')
