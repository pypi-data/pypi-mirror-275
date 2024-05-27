
#/
#
from .._quests.enumerate import enumerate_treasures
from .._quests.send_treasure_to_trends import send_treasure_to_trends
#
#
import click
#
#\

def treasures_clique ():
	@click.group ("treasures")
	def group ():
		pass


	@group.command ("enumerate")
	def enumerate ():		
		enumerate_treasures ()

	@group.command ("send")
	def enumerate ():		
		send_treasure_to_trends ()

	return group




#



