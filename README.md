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
en su directorio home se encuentran dos directorios:
    
    virtualenv/
        ....
    runtime/
        launcher.py
        log.py
        pid
        trytond.conf

El script `launcher.py` se encarga de iniciar trytond dentro del virtualenv

## TODO

 * Creación de una base de datos
 * Instalación de los modulos necesarios
 * Esquema de desarrollo, para poder probar los modulos "en vivo"

## IDEAS
 * Crear un directorio "modules" que esté linkeado al directorio modules, donde ponemos nuestros modulos custom
