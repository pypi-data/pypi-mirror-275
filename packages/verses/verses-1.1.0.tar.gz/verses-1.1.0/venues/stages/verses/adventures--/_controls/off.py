

'''
	from verses.adventures._controls.off import turn_off
	turn_off ()
'''

#----
#
from verses._essence import retrieve_essence
#
from verses.adventures.sanique._controls.off import turn_off_sanique
from verses.adventures.monetary._controls.off import turn_off_monetary_node
from verses.adventures._controls.status import check_status
#
#
import time	
#	
#----

def turn_off ():	
	essence = retrieve_essence ()

	if ("onsite" in essence ["monetary"]):
		turn_off_monetary_node ()	
	
	turn_off_sanique ()
	
	
	
	#----
	#
	#	status checks
	#
	#----
	status = check_status ()
	assert (status ["monetary"] ["local"] == "off"), status
	assert (status ["sanique"] ["local"] == "off"), status