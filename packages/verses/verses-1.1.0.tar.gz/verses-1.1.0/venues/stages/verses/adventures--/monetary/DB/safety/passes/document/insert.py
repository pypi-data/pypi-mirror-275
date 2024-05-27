




'''
	from verses.adventures.monetary.DB.safety.passes.document.insert import insert_pass
	insert_pass ({
		"document": {
			"name": "pass 1"
		}
	})
'''



from verses._essence import retrieve_essence
from verses.adventures.monetary.DB.safety.connect import connect_to_safety
	
import ships.modules.exceptions.parse as parse_exception


	
'''

'''
def insert_pass (packet):
	essence = retrieve_essence ()
	
	document = packet ["document"]
	
	try:
		[ driver, safety_DB ] = connect_to_safety ()
		passes_collection = safety_DB ["passes"]
	except Exception as E:
		print ("passes collection connect:", parse_exception.now (E))
		
	
	try:			
		inserted = passes_collection.insert_one (document)
		inserted_document = passes_collection.find_one ({ "_id": inserted.inserted_id })
		
		print ()
		print ("inserted:", inserted_document)

	except Exception as E:
		print (parse_exception.now (E))
	
		raise Exception (E)
		pass;
		
	try:
		driver.close ()
	except Exception as E:
		print (parse_exception.now (E))
		print ("food collection disconnect exception:", E)	
		
	return None;








