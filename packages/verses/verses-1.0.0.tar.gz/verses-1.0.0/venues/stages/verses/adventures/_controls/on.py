

'''
	from verses.adventures._controls.on import turn_on
	turn_on ()
'''

#----
#
from verses.adventures.sanique._controls.on import turn_on_sanique
from verses.adventures.monetary._controls.on import turn_on_monetary_node
#
from verses._essence import retrieve_essence
from verses.adventures._controls.status import check_status
#
#
import rich
#
#----

def turn_on ():	
	essence = retrieve_essence ()

	if ("onsite" in essence ["monetary"]):
		turn_on_monetary_node ()
		
	turn_on_sanique ({
		"wait_for_on": "yes"
	})	
	
	
	
	
	#----
	#
	#	status checks
	#
	#----
	status = check_status ()
	
	if ("onsite" in essence ["monetary"]):
		assert (status ["monetary"] ["local"] == "on"), status
	
	assert (status ["sanique"] ["local"] == "on"), status
	
