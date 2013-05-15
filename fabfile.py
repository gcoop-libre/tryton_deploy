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
        'build-essential',
        'postgresql-server-dev-all',
        'python-dev',
        'libxml2-dev',
        'libxslt1-dev',
        'dtach',
        ]


@_contextmanager
def virtualenv():
    """Context manager to work inside a virtualenv"""
    with settings(sudo_user=env.app_user), \
            cd(env.directory), \
            prefix("source %s/bin/activate" % env.virtualenv_directory):
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
    with settings(sudo_user=env.app_user), cd(env.directory):
        sudo("virtualenv %s" % env.virtualenv_directory)


def install_system_dependences():
    """Install apt-get based dependences"""
    run('apt-get -q update')
    run('apt-get -q install %s' % ' '.join(system_dependences))


def install_python_dependences():
    """Install all python dependences using pip"""
    reqs = 'requirements.txt'
    put(reqs, env.directory)
    with virtualenv():

        sudo('pip install -r %s --log=%s/pip.log' % (reqs, env.directory))

def install_tryton_modules():
    """Install tryton modules using pip"""
    reqs = 'modules.txt'
    put(reqs, env.directory)
    put('tryton_bootstrap.py', env.directory)
    with virtualenv():
        sudo('pip install -r %s --log=%s/pip.log' % (reqs, env.directory))
         #Bootstrapping!
        sudo('python tryton_bootstrap.py')



def start_postgres():
    """Start DB"""
    run("/etc/init.d/postgresql start")


def create_postgres_user():
    """Creates tryton user on database"""
    with settings(sudo_user="postgres"):
        sudo('createuser --createdb --no-adduser -P tryton')


def start_tryton():
    """Start tryton server in a detached enviroment"""
    put('launcher.py', env.directory)
    put('trytond.conf', env.directory)
    with cd(env.directory), settings(sudo_user=env.user):
        sudo('dtach -n /tmp/trytond python launcher.py')


def stop_tryton():
    """Stop tryton daemon"""
    pidfile = "%s/pid" % env.directory
    run("kill  $(cat %s)" % pidfile)


def disable_ipv6():
    """Disable ipv6 on target host"""
    params = [
        "net.ipv6.conf.all.disable_ipv6 = 1",
        "net.ipv6.conf.default.disable_ipv6 = 1",
        "net.ipv6.conf.lo.disable_ipv6 = 1",
        ]

    for line in params:
        run("echo %s >> /etc/sysctl.conf" % line)

    run("sysctl -p")


def deploy():
    """Run a complete deploy on a target server"""
    install_system_dependences()
    create_tryton_user()
    create_app_dirs()
    create_virtualenv()
    install_python_dependences()
    start_postgres()
    create_postgres_user()
    install_tryton_modules()
    start_tryton()


def update():
    """Update system and python packages"""
    install_system_dependences()
    install_python_dependences()
    install_tryton_modules()


def start():
    """Start an installed instance of trytond"""
    start_postgres()
    start_tryton()


def stop():
    """Stop Execution"""
    stop_tryton()
