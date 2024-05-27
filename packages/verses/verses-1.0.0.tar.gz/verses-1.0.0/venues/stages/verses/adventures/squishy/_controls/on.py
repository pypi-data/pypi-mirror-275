
'''
	from verses.adventures.squishy._controls.on import turn_on_squishy
	turn_on_squishy ()
'''

#----
#
import verses.mixes.procedure as procedure
from verses.adventures.squishy.configs import retrieve_path
#
from verses._essence import retrieve_essence
#
#----

import os
	
def turn_on_squishy (packet = {}):
	essence = retrieve_essence ()

	rubber = retrieve_path ("rubber.NFT")
	
	procedure.implicit (
		script = [
			"nft", 
			"-f",
			f"{ rubber }"
		]
	)

	os.system ("nft list ruleset")

	return;