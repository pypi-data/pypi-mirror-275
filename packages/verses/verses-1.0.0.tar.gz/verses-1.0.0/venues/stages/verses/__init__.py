
#----
#
from verses._coms.clique_pro import clique
#import verses.essence as verses_essence
#import verses.essence.moves.scan_config as config_scan
#
#
import rich
#
#
import pathlib
import inspect
import os
from os.path import dirname, join, normpath
#
#----


configured = False


def is_configured ():
	return configured

def start ():

	return;

	verses_config = config_scan.start ()
	if (verses_config == False): 
		#print ("verses_config == False")
		
		print ("The config was not found; exiting.")
		print ()
		
		exit ();
		
		return;

	print ()
	print ("configuring")
	print ()
	
	print ('merging config', verses_config)
	verses_essence.merge_config (verses_config ["configuration"])
	
	
	rich.print_json (data = verses_essence.essence)
	rich.print_json (data = verses_essence.essence)
	
	
	return;


	'''
	rich.print_json (data = {
		"verses_config": verses_config
	})
	'''
	
	'''
	verses_essence.change ("mongo", {
		"directory": ""
	})
	'''
	
	'''
		get the absolute paths
	'''
	'''
	verses_config ["configuration"] ["treasuries"] ["path"] = (
		normpath (join (
			verses_config ["directory_path"], 
			verses_config ["configuration"] ["treasuries"] ["path"]
		))
	)
	'''
	
	
	'''
		paths:
			trends
				mongo_data_1
	
	
		mongo:
			safety
				passes
				zips
				zips.files
	'''
	trends_path = normpath (join (
		verses_config ["directory_path"], 
		verses_config ["configuration"] ["trends"] ["path"]
	))
	edited_config = {
		"mints": {
			"path": normpath (join (
				verses_config ["directory_path"], 
				verses_config ["configuration"] ["mints"] ["path"]
			))
		},
		"trends": {
			"path": trends_path,
			
			"nodes": [{
				"host": "localhost",
				"port": "27017",
				"data path": normpath (join (
					trends_path, 
					"mongo_data_1"
				))
			}]
		},
		"CWD": verses_config ["directory_path"]
	}
	
	'''
	config_template = {
		
	}
	'''
	
	rich.print_json (data = {
		"edited_config": edited_config
	})

	
	verses_essence.change ("edited_config", edited_config)
	

	#print ('verses configuration', verses_config.configuration)

	'''
		Add the changed version of the basal config
		to the essence.
	'''
	'''
	config = verses_config ["configuration"];
	for field in config: 
		verses_essence.change (field, config [field])
	'''
	
	configured = True
	
	print ()
