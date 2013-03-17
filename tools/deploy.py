from fabric.api import *


env.hosts = ['flaskpi.com']
env.port = 21
# env.user = 'dev_user'
# env.password = '12345678'

WEB_USER = 'www-data'
WEB_GROUP = 'www-data'

SRC_DIR = '/var/www/flaskpi.com'


@task
def deploy():
    pass
