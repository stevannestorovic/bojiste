#!/usr/bin/bash


sudo rm -rf /var/www/html/*
echo "Cleaned old site"
sudo mv /home/bob/bojiste/_site/* /var/www/html/
echo "Moved new site, visit on web!"
