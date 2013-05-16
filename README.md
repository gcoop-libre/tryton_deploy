# Herramienta de Deploy automático para trytond

Script de deployment usando fabric. Permite crear una instancia de trytond 
funcional, con todos los modulos necesarios para produción.

El deploy solo comprende la instalación en el servidor. Las máquinas cliente,
deberan ser instaladas manualmente.

## Requisitos iniciales

Servidor objetivo Ubuntu Server 12.04.2 LTS 
Fabric instalado en la maquina que ejecuta el Script

Para ejecutar un deploy:

    fab deploy


## Detalles

En el momento del deploy se crea un nuevo usuario llamado "tryton",
en su directorio home se encuentran tres directorios:
    
    virtualenv/
        ....
    runtime/
        launcher.py
        log.py
        pid
        trytond.conf
    develop/
        ......

El script `launcher.py` se encarga de iniciar trytond dentro del virtualenv

## Modulos en desarrollo 

Para permitir trabajar con módulos que no se encuentran en PyPI,
el script contempla la utilización de repositorios git y mercurial,
consignando en el archivo develop lineas de la forma:

    git clone git://github.com/gcoop-libre/tryton_factura_electronica.git
    hg clone https://bitbucket.org/thymbra/account_ar

Para cada linea, el script de deployment ejecutara el comando e 
instalará y activara dicho módulo en la instancia de trytond

## TODO

 * Activacion de modulos necesarios
 * Esquema de desarrollo, para poder probar los modulos "en vivo"
 * Migrar paquetes de tymbra
 * Instalar paquetes de tymbra que no estan en pypi

## IDEAS
 * Crear un directorio "modules" que esté linkeado al directorio modules, donde ponemos nuestros modulos custom
