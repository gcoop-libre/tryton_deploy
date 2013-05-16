#! -*- coding: utf8 -*-

"""install tryton in a custom instance tryton modules"""
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

#Si la base de datos no existe, proteus la crea :)
config = config.set_trytond(
                            db_name,
                            'admin',
                            'postresql',
                            LANGUAGE,
                            password,
                            CONFIG_FILE
                            )

#Obtengo todos los modulos instalados!

Module = Model.get('ir.module.module')
modules = Module.find()  # Obtengo todos
Module.install([m.id for m in modules], config.context)

Wizard('ir.module.module.install_upgrade').execute('upgrade')
