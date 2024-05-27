


'''	
	from verses.frontiers.adventures_trends.monetary.DB.verses_inventory.connect import connect_to_verses_inventory
	[ driver, DB_verses_trends ] = connect_to_verses_inventory ()
	driver.close ()
'''

'''
	from verses.frontiers.adventures_trends.monetary.DB.verses_inventory.connect import connect_to_verses_inventory
	[ driver, DB_verses_trends ] = connect_to_verses_inventory ()
	ion_bits = DB_verses_trends ["bits"]	
	driver.close ()
'''




from verses.frontiers.adventures_trends.monetary.moves.URL.retrieve import retreive_monetary_URL
from verses._essence import retrieve_essence
	
import pymongo

def connect_to_verses_inventory ():
	essence = retrieve_essence ()
	
	ingredients_DB_name = essence ["trends"] ["monetary"] ["databases"] ["verses_trends"] ["alias"]
	monetary_URL = retreive_monetary_URL ()

	driver = pymongo.MongoClient (monetary_URL)

	return [
		driver,
		driver [ ingredients_DB_name ]
	]