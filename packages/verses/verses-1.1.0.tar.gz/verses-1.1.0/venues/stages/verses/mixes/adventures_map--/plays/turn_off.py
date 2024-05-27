

'''
	turn_off ({
		
	})
'''

from ..utilities.map.scan import scan_map

def turn_off (packet):
	the_map = packet ["the_map"]
	with open (the_map, 'r') as FP:
		bracket = json.load (FP)

	print ("bracket:", bracket)