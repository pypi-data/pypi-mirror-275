




'''
	verses treasures send --name "treasure.1" --version 1.0.0
'''

'''
	objective:
		send_treasure_to_trends ({
			"treasure": {
				"name": "treasure.1",
				"version": "1.0.0"
			}
		})
	
		the procedure:
			[ ] search the treasures
'''

'''
	
'''

from verses.frontiers.adventures_treasures._quests.enumerate import enumerate_treasures
	
from verses._essence import retrieve_essence


def send_treasure_to_trends (packet):
	essence = retrieve_essence ()

	treasure = packet ["treasure"]
	name = treasure ["name"] 
	version = treasure ["version"] 
	
	treasures = enumerate_treasures ()

	return;