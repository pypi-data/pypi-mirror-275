

from ..utilities.hike_passive import hike_passive
from ..utilities.map.etch import etch_map
	
from ..utilities.map.etch import scan_map

	

'''
	{
		"name": "adventure_1",
		"turn on": {
			"adventure": "python3 -m http.server 8080",
			"kind": "process identity"
		}
	}
'''
def turn_on (packet):
	print ("packet:", packet)
	adventures = packet ["adventures"]
	the_map = packet ["map"]

	#
	#	check the map to make sure the process isn't already on
	#
	#
	scan_map ({
		"path": the_map,
		"bracket": {}
	})
	

	adventures_map_bracket = {}
	for adventure in adventures:
		adventure_script = adventure ["turn on"] ["adventure"]
		kind = adventure ["turn on"] ["kind"]
		name = adventure ["name"]
	
		process = hike_passive ({
			"script": adventure_script
		})
		
		if (kind == "process identity"):
			adventures_map_bracket [ name ] = {
				"kind": kind,
				"process_identity": process ["process_identity"]
			}
		
		else:
			adventures_map_bracket [ name ] = {
				"kind": kind
			}

	
	etch_map ({
		"path": the_map,
		"bracket": adventures_map_bracket
	})
	
	return adventures_map_bracket