#!/usr/bin/env python
# -*- coding:utf8 -*-

# FIXME demonizar de la manera apropiada

activate_this = "/home/tryton/virtualenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

def database_list():
    """Fetch all databases in current instance"""
    from trytond.backend import Database
    database = Database().connect()
    cursor = database.cursor()
    databases = database.list(cursor)
    cursor.close()
    return databases

import trytond
from trytond.config import CONFIG

options = {
    'init': {},
    'update': {},
    'configfile': '/home/tryton/runtime/trytond.conf',
    'db_name': [],
    'logfile': '/home/tryton/runtime/tryton.log',
    'pidfile': '/home/tryton/runtime/pid'
    }

server = trytond.server.TrytonServer(options)

# Parametrization of db to update
CONFIG['db_name'] = database_list()
CONFIG['update']['all'] = 1

server.run()
