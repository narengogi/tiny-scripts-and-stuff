#!/bin/bash


date +"%m/%d/%Y %H:%M:%S $HOSTNAME" >>  /var/log/hardware_access_log.txt
lsof /dev/snd/pcmC0D0c >>  /var/log/hardware_access_log.txt
echo "---------------" >>  /var/log/hardware_access_log.txt

