#! -*- coding: utf8 -*-

"""install tryton in a custom instance tryton modules"""

import warnings

import getpass
from proteus import config, Model, Wizard

CONFIG_FILE = '/home/tryton/runtime/trytond.conf'
LANGUAGE = 'es_AR'

db_name = raw_input('Ingrese el nombre de la base de datos [default]: ')
if not db_name:
    db_name = 'default'

password = getpass.getpass(
    "Ingrese el password de admin a utilizar en la base '%s': " % db_name
    )

#if database doesn't exists, proteus creates it
config = config.set_trytond(
                            db_name,
                            'admin',
                            'postgresql',
                            LANGUAGE,
                            password,
                            CONFIG_FILE
                            )

#Tryton throw a lot of deprecation warnings, we turn these off
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)

    Module = Model.get('ir.module.module')
    #Get all installed modules
    modules = Module.find()
    Module.install([m.id for m in modules], config.context)
    Wizard('ir.module.module.install_upgrade').execute('upgrade')
