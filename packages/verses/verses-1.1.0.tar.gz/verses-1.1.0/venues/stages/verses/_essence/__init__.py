

'''
	from verses._essence import build_essence
	build_essence ()
	
	build_essence ({
		"essence_path": ""
	})
'''

'''
	from verses._essence import retrieve_essence
	essence = retrieve_essence ()
'''

'''
	from verses._essence import receive_monetary_URL
	monetary_URL = receive_monetary_URL ()
'''




'''
	objective:
		[ ] harbor pid for starting and stopping:
				"PID_path": crate ("harbor/the.process_identity_number")
'''


#----
#
from .seek import seek_essence
from .scan import scan_essence
from .merge import merge_essence
from .prefab import retrieve_prefab
#
#
import rich
import pydash
#
#
import pathlib
from os.path import dirname, join, normpath
import sys
import os
#
#----


essence = {}
essence_built = "no"

def build_essence (* positionals):
	global essence_built;
	if (essence_built == "yes"):
		return;
	
	essence_path = ""
	if (len (positionals) >= 1):
		if ("essence_path" in positionals [0]):
			essence_path = positionals [0] ["essence_path"]

	if (len (essence_path) == 0):
		essence_path = seek_essence ({
			"name": "essence_verses.py"
		})
	
	external_essence = scan_essence (essence_path)
	internal_essence = merge_essence (
		retrieve_prefab ({
			"essence_path": essence_path
		}),
		external_essence
	)

	for key in internal_essence:
		essence [ key ] = internal_essence [key]

	essence_built = "yes"

	return;


#
#	Use this; that way can easily
# 	start using redis or something.
#
def retrieve_essence ():
	build_essence ()
	return essence


