

import os
from verses._essence import retrieve_essence

import rich

def list_directories (directory):
	directories = []
	anomalies = []

	places = os.listdir (directory)
	for place in places:
		full_path = os.path.join (directory, place)
		
		if (os.path.isdir (full_path)):
			directories.append (place)
		else:
			raise Exception (f"A non-directory was found at: { place }")

	return {
		"directories": directories,
		"anomalies": anomalies
	}
	
def split_last_substring(string):
	last_dot_index = string.rfind ('.')

	if last_dot_index != -1:
		part_before = string [:last_dot_index]
		part_after = string [last_dot_index + 1:]
		return [ part_before, part_after ]
	
	raise Exception (f"A non-dot directory name was found: { string }")

def enumerate_treasures ():
	essence = retrieve_essence ()
	treasures_path = essence ["treasures"] ["path"]

	proceeds = list_directories (treasures_path)
	directories = proceeds ["directories"]
	anomalies = proceeds ["anomalies"]
	
	treasures = []
	for directory in directories:
		#print ("directory:", directory)
		
		parts = split_last_substring (directory)
		treasures.append (parts)
		
		
	rich.print_json (data = treasures)	
		



	return;