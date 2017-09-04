# coding: utf-8

from gevent import monkey
monkey.patch_all()

import os
# 设置 Django 项目配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import leancloud
from gevent.pywsgi import WSGIServer

from django.core.wsgi import get_wsgi_application
from leancloud import Engine


engine = Engine(get_wsgi_application())

APP_ID = os.environ['LC_APP_ID']
#APP_ID= '8xzeqKMnJ6yd52gE5iW2Ko7Q-gzGzoHsz'
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
#MASTER_KEY = 'Hk9mAXLJW3fpzvRQ21mKcqAU'
PORT = int(os.environ['LC_APP_PORT'])
#PORT = 4000
leancloud.init(APP_ID, master_key=MASTER_KEY)

# application = engine
SECRET_KEY = 'fnd65yp+^rq+6gs%omd+c2p&jtifow&eclauf-ox3^&t!n6*$%'
application = leancloud.engine.CookieSessionMiddleware(engine, secret=SECRET_KEY.encode('utf-8'), fetch_user=True)

if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    server = WSGIServer(('127.0.0.1', PORT), application)
    server.serve_forever()
