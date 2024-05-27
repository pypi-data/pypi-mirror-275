

#/
#
import pathlib
from os.path import dirname, join, normpath
import os
import sys
#
#\

this_directory = pathlib.Path (__file__).parent.resolve ()	
the_mix_directory = str (normpath (join (this_directory, "../..")));
the_verses_process = str (normpath (join (this_directory, "../__bin/verses_1")))


def retrieve_prefab (packet):
	essence_path = packet ["essence_path"]

	essence_directory = str (os.path.dirname (essence_path))

	mints_directory = str (normpath (join (essence_directory, "mints")));
	trends_directory = str (normpath (join (essence_directory, "trends")));
	treasures_directory = str (normpath (join (essence_directory, "treasures")));
	

	CWD = os.getcwd ();

	return {
		"essence_path": essence_path,
		"essence_directory": essence_directory,
		"CWD": os.getcwd (),
		
		#
		#	summary in goodest.mixes.activate_alert
		#
		"alert_level": "caution",
		
		#
		#	modes: [ "nurture", "business" ]
		#
		"mode": "business",
		
		"the_show": the_verses_process,
	
	
		"ventures": {
			"path": str (normpath (join (this_directory, "ventures_map.JSON")))
		},
		
		"mints": {
			"path": mints_directory
		},
		"treasures": {
			"path": treasures_directory
		},
	
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
			"path": trends_directory,
			
			"emphemeral": {
				"path": str (normpath (join (trends_directory, "[emphemeral]"))),
			},
			
			"monetary": {
				"URL": "mongodb://0.0.0.0:39000/",
				
				"node": {
					"local": "yes",
					
					"path": str (normpath (join (
						trends_directory, 
						"[monetary]"
					))),
					"data_path": str (normpath (join (
						trends_directory, 
						"[monetary]/data"
					))),
					"logs_path": str (normpath (join (
						trends_directory, 
						"[monetary]/logs/the.logs"
					))),
					"PID_path": str (normpath (join (
						trends_directory, 
						"[monetary]/the.process_identity_number"
					))),
					
					"host": "0.0.0.0",
					"port": "39000"
				},
				
				
				"databases": {
					"verses_trends": {
						"alias": "verses_trends",
						"collections": [
							"treasures",
							
							#
							#	GridFS
							#
							#
							"bits",
							"bits.files"
						]
					}
				},
				"saves": {
					"path": str (normpath (join (
						trends_directory, 
						"[monetary_saves]"
					))),
					"exports": {
						"path": str (normpath (join (
							trends_directory, 
							"[monetary_saves]/exports"
						)))						
					},
					"dumps": {
						"path": str (normpath (join (
							trends_directory, 
							"[monetary_saves]/dumps"
						)))
					}					
				}
			}
		},

		"dictionary": {
			"path": str (normpath (join (the_mix_directory, "____glossary"))),
			"goodest": str (normpath (join (the_mix_directory, "____glossary/verses_1"))),
		}
	}