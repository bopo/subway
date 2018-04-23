# -*- coding: utf-8 -*-

import os
import fabric
from fabric.api import cd, env, local, run, task
from fabric.contrib import project
import environ

conf = environ.Env()
conf.read_env()

env.roledefs = {
    'dev': ['root@103.200.97.197'],
    'pre': ['root@103.200.97.197'],
}

env.excludes = (
    "*.pyc", "*.db", ".DS_Store", ".coverage", ".git", ".hg", ".tox", ".idea/",
    'assets/', 'runtime/', 'db.sqlite3', 'tests', 'docs', '__pycache__',
    'env.docker', 'env.server', 'docs')

env.remote_dir = conf('ENV_REMOTE_DIR', default='/home/site/sensor/server')
env.local_dir = conf('ENV_LOCAL_DIR', default='.')

def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

@task
def mock():
    '''填充 mock 数据'''
    local('make build')


@task
def init():
    '''远程初始化 docker 部署'''
    run('make build')
    run('make setup')
    run('make docs')

@task
def load(name='all'):
    ''' 导入开发数据 '''
    run('python manage.py loaddata config/fixtures/{}.json'.format(name))

@task
def dump(app=''):
    ''' 导出开发数据 '''
    local('python manage.py dumpdata {} > config/fixtures/{}.json'.format(
        app, (app if app else 'all')))

@task
def pipv():
    '''更新 requirements.txt 内的版本'''
    local('pip freeze > freeze.txt')

    freezes = parse_requirements('freeze.txt')
    require = parse_requirements('requirements.txt')

    freeze = dict([line.split("==") for line in freezes])
    requir = ['{}=={}'.format(line, freeze[line]) for line in require if line and freeze.get(line, None)]
    
    local('rm -rf requirements.lock')

    with open('requirements.lock', 'a') as f:
        f.writelines([line + "\n" for line in requir])

    local('rm -rf freeze.txt')

@task
def wsgi(worker='egg:meinheld#gunicorn_worker', host='127.0.0.1', port=5000):
    local('DJANGO_SETTINGS_MODULE=config.settings.pre gunicorn config.wsgi:application -k {worker} -w 4 -b {host}:{port}'.format(
        worker=worker, host=host, port=port))

@task
def unix():
    '''文本文件 windows 格式转 unix 格式'''
    local('find . "*.txt" | xargs dos2unix')
    local('find . "*.md" | xargs dos2unix')
    local('find . "*.py" | xargs dos2unix')
    local('dos2unix Makefile')


@task(alias='ci')
def gc():
    '''提交源码仓库(git commit)'''
    local('git commit -m "first commit"')


@task
def gp(branch='develop'):
    '''推送源码仓库(git push)'''
    local('git push -u origin {}'.format(branch))


@task
def stat():
    '''更新静态文件'''
    with cd(env.remote_dir):
        run('python manage.py collectstatic --noinput')

@task
def lst():
    '''更新静态文件'''
    local('python manage.py collectstatic --noinput')

@task
def push():
    '''同步服务器代码'''
    project.rsync_project(
        remote_dir=env.remote_dir,
        local_dir=env.local_dir,
        exclude=env.excludes,
        delete=False
    )


@task
def migr():
    '''合并数据文件'''
    with cd(env.remote_dir):
        run('''python manage.py migrate''')


@task()
def init():
    '''初始化服务'''

    project.rsync_project(
        remote_dir=env.remote_dir,
        local_dir=env.local_dir,
        exclude=env.excludes,
        delete=True
    )

    run('/usr/bin/supervisorctl device start')


@task()
def rest():
    '''重启服务'''
    run('/usr/bin/supervisorctl restart device')


@task
def stop():
    '''停止服务'''
    run('/usr/bin/supervisorctl device stop')

@task
def prod():
    '''文件打包'''
    local('tar zcfv ./prod.tgz '
          '--exclude=.git '
          '--exclude=.tox '
          '--exclude=.svn '
          '--exclude=.env '
          '--exclude=.idea '
          '--exclude=*.tgz '
          '--exclude=*.pyc '
          '--exclude=.vagrant '
          '--exclude=tests '
          '--exclude=assets/media/* '
          '--exclude=assets/static/* '
          '--exclude=runtime/* '
          '--exclude=vendors '
          '--exclude=config/fixtures '
          '--exclude=env.* '
          '--exclude=.DS_Store '
          '--exclude=.phpintel '
          '--exclude=.template '
          '--exclude=db.sqlite3 '
          '--exclude=Makefile '
          '--exclude=pytest.ini '
          '--exclude=README.md '
          '--exclude=Pipfile '
          '--exclude=Pipfile.lock '
          '--exclude=fabfile.py '
          '--exclude=Vagrantfile .')

@task
def pack():
    '''文件打包'''
    local('tar zcfv ./pack.tgz '
          '--exclude=.git '
          '--exclude=.tox '
          '--exclude=.env '
          '--exclude=.idea '
          '--exclude=*.tgz '
          '--exclude=*.pyc '
          '--exclude=.vagrant '
          '--exclude=assets/media/* '
          '--exclude=assets/static/* '
          '--exclude=runtime/* '
          '--exclude=.DS_Store '
          '--exclude=.phpintel '
          '--exclude=.template '
          '--exclude=db.sqlite3 '
          '--exclude=Vagrantfile .')
