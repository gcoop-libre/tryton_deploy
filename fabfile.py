#! -*- coding: utf8 -*-

from __future__ import with_statement
from fabric.api import run, cd, prefix, env, put, sudo, settings
#from fabric.contrib.console import confirm


from contextlib import contextmanager as _contextmanager

env.hosts = ["root@192.168.10.139"]

env.directory = "/home/tryton/runtime"
env.virtualenv_directory = "/home/tryton/virtualenv"
env.app_user = "tryton"

system_dependences = [
       'python-setuptools',
       'python-virtualenv',
       'postgresql',
        ]



@_contextmanager
def virtualenv():
    """Context manager to work inside a virtualenv"""
    with cd(env.directory), \
            prefix("source %s/bin/activate" % env.virtualenv_directory), \
            settings(sudo_user=env.app_user):
            yield


def create_tryton_user():
    """Create aplication user"""
    run('adduser %s' % env.app_user)

def create_app_dirs():
    """Create app dirs"""
    with settings(sudo_user=env.app_user):
        sudo('mkdir %s' % env.directory)
        sudo('mkdir %s' % env.virtualenv_directory)

def create_virtualenv():
    with settings(sudo_user=env.app_user):
        sudo("virtualenv %s" % env.virtualenv_directory)


def install_system_dependences():
    """Install apt-get based dependences"""
    run('apt-get update')
    run('apt-get install %s' % ' '.join(system_dependences))

def install_python_dependences():
    """Install all python dependences using pip"""
    put('requirements.txt', env.directory)
    with virtualenv():
        sudo('echo requirements.txt')


def deploy():
    install_system_dependences()
    create_tryton_user()
    create_app_dirs()
    create_virtualenv()
    install_python_dependences()

def test():
    install_system_dependences()
    create_virtualenv()
    install_python_dependences()

