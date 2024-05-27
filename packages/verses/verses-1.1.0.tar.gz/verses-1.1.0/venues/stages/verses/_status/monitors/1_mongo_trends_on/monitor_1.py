
'''
	can save and retrieve a mint
'''

import verses
from verses._essence import retrieve_essence

import verses.modules.moves.trends.status as trends_status
	
def check_1 ():
	essence = retrieve_essence ()
	
	verses.start ()
	the_status = trends_status.check_status ()
	print ("the_status:", the_status)

	return;
	
	
checks = {
	'check 1': check_1
}