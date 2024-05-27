

#----
#
import pathlib
from os.path import dirname, join, normpath
import sys
import os
#
#----

this_directory = pathlib.Path (__file__).parent.resolve ()	
the_mix_directory = str (normpath (join (this_directory, "../..")));
the_verses_process = str (normpath (join (this_directory, "../__bin/verses_1")))

CWD = os.getcwd ();
trends_path = str (normpath (join (CWD, "trends")))



def retrieve_prefab (packet):
	essence_path = packet ["essence_path"]

	return {
		"essence_path": essence_path,
		
		#
		#	summary in goodest.mixes.activate_alert
		#
		"alert_level": "caution",
		
		#
		#	modes: [ "nurture", "business" ]
		#
		"mode": "business",
		
		"the_show": the_verses_process,
	
		#
		#	trends
		#		node_1
		#			mongo_data
		#			mongod.pid
		#			logs.log
		#
		#	DB:safety
		#		ion:passes
		#		ion:zips
		#		ion:zips.files
		#
		"trends": {
			"path": "trends",
			
			"mongo": {
				"nodes": [{
					"rel_path": "node_1",
					
					"host": "localhost",
					"port": "27017",
					
					"PID_file_name": "mongod.pid",
					"log_file_name": "logs.log",
				}], 

				"DB_name": 'safety',
				"passes": {
					"collection": "passes",
					"GridFS_zips": 'zips',
					"GridFS_zips_files": 'zips.files'
				}
			}	
		},
		
		"CWD": os.getcwd (),
		
		#"vv_turbo": {
		#	"dist_path": str (normpath (join (
		#		the_mix_directory, 
		#		"adventures/vv_turbo/apps/web/the_build"
		#	)))
		#},

		
		"monetary": {
			"databases": {
				"safety": {
					"alias": "safety",
					"collections": [
						"passes",
						"squeezes"
					]
				}
			},
			
			#
			#	_saves
			#		
			#
			"saves": {
				"path": str (normpath (join (
					trends_path, 
					"[saves]"
				))),
				"exports": {
					"path": str (normpath (join (
						trends_path, 
						"[saves]/exports"
					)))						
				},
				"dumps": {
					"path": str (normpath (join (
						trends_path, 
						"[saves]/dumps"
					)))
				}					
			}
		},
		
		
		
		"sanique": {
			"directory": str (normpath (join (
				the_mix_directory, 
				"adventures/sanique"
			))),
			
			"path": str (normpath (join (
				the_mix_directory, 
				"adventures/sanique/harbor/on.proc.py"
			))),
			
			"port": "8000",
			"host": "0.0.0.0",
			
			#
			#	don't modify these currently
			#
			#	These are used for retrieval, but no for launching the
			#	sanic inspector.
			#
			#	https://sanic.dev/en/guide/running/inspector.md#inspector
			#
			"inspector": {
				"port": "7457",
				"host": "0.0.0.0"
			}
		},
		"dictionary": {
			"path": str (normpath (join (the_mix_directory, "__dictionary"))),
			"goodest": str (normpath (join (the_mix_directory, "__dictionary/goodest"))),
		}
	}