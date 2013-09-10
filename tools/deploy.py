from fabric.api import *
from fabric.operations import run, put

env.hosts = ['flaskpi.com']
env.port = 22
env.user = 'e0ne'
# env.password = '12345678'

WEB_USER = 'www-data'
WEB_GROUP = 'www-data'

SRC_DIR = '/home/e0ne/web/flaskpi'


@task
def deploy(src):
    content = ['etc', 'flaskpi', 'static', 'templates',
               'tools', 'tutorials', '*.py']
    for item in content:
        put('{0}/{1}'.format(src, item), SRC_DIR)
