

'''
def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_folder = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

add_paths_to_system ([
	'../../../structures_pip'
])
'''


import pathlib
from os.path import dirname, join, normpath
import sys

this_folder = pathlib.Path (__file__).parent.resolve ()
venues = normpath (join (this_folder, "../../../../venues"))

monitors = str (normpath (join (this_folder, "monitors")))


if (len (sys.argv) >= 2):
	glob_string = monitors + '/' + sys.argv [1]
else:
	glob_string = monitors + '/**/monitor_*.py'

import biotech

scan = biotech.start (
	glob_string = glob_string,
	simultaneous = True,
	module_paths = [
		normpath (join (venues, "stages")),
		normpath (join (venues, "structures_pip"))
	],
	relative_path = monitors
)



#
#
#