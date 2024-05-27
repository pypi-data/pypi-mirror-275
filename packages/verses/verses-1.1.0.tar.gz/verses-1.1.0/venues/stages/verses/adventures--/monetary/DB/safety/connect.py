




'''	
	from verses.adventures.monetary.DB.safety.connect import connect_to_safety
	[ driver, safety_DB ] = connect_to_safety ()
	driver.close ()
'''

'''
	from verses.adventures.monetary.DB.safety.connect import connect_to_safety
	[ driver, safety_DB ] = connect_to_safety ()
	passes_collection = safety_DB ["passes"]	
	driver.close ()
'''




from verses.adventures.monetary.utilities.URL.retrieve import retreive_monetary_URL
from verses._essence import retrieve_essence
	
import pymongo

def connect_to_safety ():
	essence = retrieve_essence ()
	ingredients_DB_name = essence ["monetary"] ["databases"] ["safety"] ["alias"]
	
	monetary_URL = retreive_monetary_URL ()

	driver = pymongo.MongoClient (monetary_URL)

	return [
		driver,
		driver [ ingredients_DB_name ]
	]