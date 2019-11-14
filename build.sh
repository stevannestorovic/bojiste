#!/usr/bin/env bash

./make_cats.py
bundle exec jekyll b
sudo rm -rf /var/www/html/*
sudo mv _site/* /var/www/html/
