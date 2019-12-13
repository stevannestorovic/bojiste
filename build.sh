#!/usr/bin/env bash

echo "[i] Building pages..."
./make_cats.py > /dev/null
echo "[+] Done building pages."
echo "[i] Building jekyll site"
bundle exec jekyll b
echo "[+] Jekyll build done"
echo "[i] Moving files to /var/www/html"
sudo rm -rf /var/www/html/*
sudo mv _site/* /var/www/html/
echo "[+] Files movede"
echo "[+] Site is online, visit at http://178.128.150.79"
