#!/usr/bin/env python3

import yaml
import os
import sys

CATS = ''

with open('../_data/cats.yml') as f:
	CATS = yaml.safe_load(f)


for cat in CATS:
	print(cat['maincat'])
	try:
		for subcat in cat['subcats']:
			print('    ' + subcat['name'])
			try:
				for subsubcat in subcat['subsubcats']:
					print('        ' + subsubcat)
			except:
				pass
	except:
		pass

