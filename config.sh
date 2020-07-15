#!/bin/bash

echo "initializing config..." >> /home/pi/doorman/log_config.txt
echo "initializing ssh..." >> /home/pi/doorman/log_config.txt
sudo systemctl enable ssh
sudo systemctl start ssh
echo "config finished..." >> /home/pi/doorman/log_config.txt


