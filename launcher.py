#!/usr/bin/env python
# -*- coding:utf8 -*-

# FIXME demonizar de la manera apropiada

activate_this = "/home/tryton/virtualenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

import trytond
options = {
    'init': {},
    'update': {},
    'configfile': None,
    'db_name': [],
    'logfile': '/home/tryton/runtime/tryton.log',
    'pidfile': '/home/tryton/runtime/pid'
    }

trytond.server.TrytonServer(options).run()
