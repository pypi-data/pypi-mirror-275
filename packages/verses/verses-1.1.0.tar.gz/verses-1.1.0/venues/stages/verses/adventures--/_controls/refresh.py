

'''
	from verses._controls.refresh import refresh
	refresh ()
'''

#----
#
from verses.adventures.sanique._controls.refresh import refresh_sanique
#	
from verses._essence import retrieve_essence
from verses.adventures._controls.status import check_status
#
import rich
#
#----

def refresh ():	
	essence = retrieve_essence ()

	#if ("onsite" in essence ["monetary"]):
	#	turn_on_monetary_node ()
		
	refresh_sanique ()	
		
	check_status ()
		
