

'''
	from verses._controls.status import check_status
	check_status ()
'''

#----
#
from verses._essence import retrieve_essence
from verses.adventures.monetary.utilities.URL.retrieve import retreive_monetary_URL
from verses.adventures.sanique._controls.status import check_sanique_status
from verses.adventures.monetary._controls.status import check_monetary_status
from verses.mixes.docks.address import find_container_address
#
#
from biotech.topics.show.variable import show_variable
#
#
import rich
#
#----

def check_status ():	
	essence = retrieve_essence ()

	the_monetary_status = ""
	if ("onsite" in essence ["monetary"]):
		the_monetary_status = check_monetary_status ()
		
	the_sanic_status = check_sanique_status ()
	
	address = find_container_address ()
	
	the_status = {
		"address": address,
		"monetary": {
			"URL": retreive_monetary_URL (),
			"local": the_monetary_status
		},
		"sanique": {
			"port": essence ["sanique"] ["port"],
			"local": the_sanic_status
		}
	}
	
	show_variable ({
		"statuses": the_status
	})
	
	return the_status