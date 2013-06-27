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

## Como se usa

El script no debe ejecutarse en el servidor, sino que define un conjunto 
de *comandos remotos* a ejecutar en la maquina servidor.

Dentro del archivo `fabfile.py` se encuentran definidos los comandos, y la 
lista `env.hosts` que contiene un listado de los servidores donde se va a 
deployar la aplicacion. Si la linea está comentada, nos pide por la linea de 
comandos el string de conexion al servidor, por ejemplo "root@fontar"

## Comandos implementados

```
☁  tryton_deploy [master] ⚡ fab -l              

Deployment script for tryton on ubuntu 12.04 LTS
Theoretically it can work on any apt-get based GNU/Linux distro

Available commands:

    bootstrap                   Creates a new tryton db, and activate all installed modules
    copy_module                 Copy a module inside trytond modules dir
    deploy                      Run a complete deploy on a target server
    drop_all                    Drop all databases in the instance
    install_develop_modules     Install git and hg modules in trytond
    install_python_dependences  Install all python dependences using pip
    install_system_dependences  Install apt-get based dependences
    install_tryton_modules      Install tryton modules using pip
    restart                     Restart the instance
    start                       Start an installed instance of trytond
    stop                        Stop Execution
    update                      Update system and python packages
    update_all_modules          Update all databases in the instance
```
 
## Detalles

En el momento del deploy se crea un nuevo usuario lulamado "tryton",
en su directorio home se encuentran tres directorios:
    
    virtualenv/
        ....
    runtime/
        launcher.py
        log.log
        pid
        trytond.conf
    develop/
        ......

Todos los scripts de lanzamiento están dentro del directorio `runtime`, 
en el directorio `develop`, estan los repositorios git o mercurial de los
modulos que no estan en **PyPI**

## Modulos en desarrollo 

Para permitir trabajar con módulos que no se encuentran en PyPI,
el script contempla la utilización de repositorios git y mercurial,
consignando en el archivo develop lineas de la forma:

    git clone git://github.com/gcoop-libre/tryton_factura_electronica.git
    hg clone https://bitbucket.org/thymbra/account_ar

Para cada linea, el script de deployment ejecutara el comando e 
instalará y activara dicho módulo en la instancia de trytond
