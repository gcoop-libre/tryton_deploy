# Herramienta de Deploy automático para trytond

Script de deployment usando fabric. Permite crear una instancia de trytond 
funcional, con todos los modulos necesarios para produción.

El deploy solo comprende la instalación en el servidor. Las máquinas cliente,
deberan ser instaladas manualmente.

## Requisitos iniciales

Servidor objetivo Ubuntu Server 12.04.2 LTS 
Fabric instalado en la maquina que ejecuta el Script

## Instalar dependencias

Las dependencias de paquete son las siguientes:
    
    python-distribute
    postgresql

## Detalles

En el momento del deploy se crea un nuevo usuario llamado "tryton",
en su directorio home se encuentran dos directorios:
    
    virtualenv
    runtime

que contienen los componentes de la aplicacion



