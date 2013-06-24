#!/bin/sh
current_user=$(whoami);
script_user='tryton'

if [ $current_user != $script_user ]; then
    echo "This script has to run with tryton user";
    exit 1;
fi;


if [ -f pid ]; then
    echo "Stoping Actual instance";
    kill $(cat pid);
    sleep 2;
fi;

dtach -n /tmp/trytond python launcher.py;
