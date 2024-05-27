#!/usr/bin/python3

'''
	~/adventures/verses-tavern
	
	nano ~/adventures/verses-tavern
		#!/usr/bin/python3
		python3 /media/treasury-1/water/status600.com/pypi/reptilian_essences/modules_series_4/verses/modules/structures/verses/bin/verses-tavern.py
	
	
	PATH=$PATH:/media/treasury-1/water/status600.com/pypi/reptilian_essences/modules_series_4/verses/modules/structures/verses/bin
	
	verses-tavern
'''

import pathlib
from os.path import dirname, join, normpath
import sys
def add_paths_to_system (paths):	
	this_folder = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

add_paths_to_system ([
	'../../structures',
	'../../structures_pip'
])

import verses
verses.clique ()