

'''
	apt install nftables
'''


'''
	from verses.adventures.squishy._controls.build import build_squishy
	build_squishy ()
'''

#----
#
import verses.mixes.procedure as procedure
from verses.adventures.squishy.configs import retrieve_path
#
from verses._essence import retrieve_essence
#
#
import os
#
#----


	
def build_squishy (packet = {}):
	essence = retrieve_essence ()
	os.system ("apt install nftables -y")
	return;