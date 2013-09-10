from fabric.api import *
from fabric.operations import run, put

env.hosts = ['e0ne@flaskpi.com']
env.port = 22
env.user = 'jenkins'
# env.password = '12345678'

WEB_USER = 'www-data'
WEB_GROUP = 'www-data'

SRC_DIR = '/home/e0ne/web/flaskpi'


@task
def deploy(src):
    put(src, SRC_DIR)
