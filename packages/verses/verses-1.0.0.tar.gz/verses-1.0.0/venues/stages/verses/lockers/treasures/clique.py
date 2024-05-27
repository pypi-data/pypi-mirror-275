


#----
#
#
from verses._essence import build_essence, retrieve_essence
#
from .quests.enumerate import enumerate_treasures
from .quests.store_as_trend import store_as_trend
#
#
import click
#
#----

def clique_treasures ():

	@click.group ("treasures")
	def group ():
		pass

	
	#
	#	verses on
	#
	@group.command ("enumerate")
	def enumerate ():		
		essence = retrieve_essence ()
		
		enumerate_treasures ()
		
		#print ("treasures path:", essence ["treasures"] ["path"])
	
		return;
	
	
	@group.command ("store-as-trend")
	def enumerate ():		
		essence = retrieve_essence ()
		
		store_as_trend ()
		
		
	
		return;


	return group




#



