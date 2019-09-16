#!/usr/bin/env python3
import os
import sys

CAT_FILE = "_data/categories.yml"
BRAND_FILE = "_data/brands.yml"


cats = open(CAT_FILE, "r")
brands = open(BRAND_FILE, "r")

for line in cats.readlines():
	if "name" in line:
		name = line.split('"')[1]
		name = name.replace(" ", "_")
		os.system('rm {}.html'.format(name))


for line in brands.readlines():
	if "name" in line:
		name = line.split('"')[1]
		name = name.replace(" ", "_")
		os.system('rm {}.html'.format(name))
