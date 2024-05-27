

'''
	import verses.modules.moves.trends.status as trends_status
	the_status = trends_status.check_status ()
	
	
	# "on" or "off"
'''


from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from verses._essence import retrieve_essence
	
def check_status ():
	try:
		essence = retrieve_essence ()
	
		mongo = verses_essence.connect ()
		mongo.admin.command ('ismaster')
		print("Mongo is on.")
		
		return "on"
		
	except ConnectionFailure:
		pass;
	
	print ("A connection to mongo could not be established.")
	
	return "off"
