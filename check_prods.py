#!/usr/bin/env python3

import os
import sys
import yaml

files = os.listdir('_products')

for f in files:
	with open('_products/' + f, 'r') as fo:
		lines = fo.readlines()
		lines = lines[1:len(lines)-2]
		y_string = ''
		for l in lines:
			y_string += l
		yaml_data = yaml.safe_load(y_string)
		yd = yaml.safe_load(y_string)

	if 'sifra' not in yd.keys() or yd['sifra'] == '':
		print(yd)
		print(f + ' is corrupt')
		input('')
