#!/bin/bash

# Este script está rodando no /etc/xdg/lxsession/LXDE-pi/autostart
echo "executing script..." >> /home/pi/doorman/log_starting.txt
export PYTHONUNBUFFERED=1;
cd /home/pi/doorman
echo "executing remote_door.py..." >> /home/pi/doorman/log_starting.txt
stdbuf -oL python3 -u remote_door.py | tee -a log.txt 2>&1;

