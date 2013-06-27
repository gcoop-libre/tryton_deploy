#!/usr/bin/env python
# -*- coding:utf8 -*-

activate_this = "/home/tryton/virtualenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))
def drop_all():
    from trytond.backend import Database
    database = Database().connect()
    cursor = database.cursor()
    erase_cursor = database.cursor(autocommit=True)
    for db in database.list(cursor):
        print "Dropping database %s" % db
        database.drop(erase_cursor, db)
    erase_cursor.close()
    cursor.close()

import trytond

options = {
    'init': {},
    'update': {},
    'configfile': '/home/tryton/runtime/trytond.conf',
    'db_name': [],
    'logfile': '/home/tryton/runtime/tryton.log',
    'pidfile': '/home/tryton/runtime/pid'
    }

#we instance a server, for enviroment initiaization
server = trytond.server.TrytonServer(options)
drop_all()

