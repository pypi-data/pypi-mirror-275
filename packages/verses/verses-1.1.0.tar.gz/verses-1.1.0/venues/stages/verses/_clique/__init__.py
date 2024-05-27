




#from .group import clique as clique_group







#/
#
import verses
from .group.trends import trends_clique
import verses.modules.moves.save as save
#
from verses.frontiers.ventures import retrieve_ventures
from verses.frontiers.adventures_treasures._controls._clique import treasures_clique
from verses.frontiers.adventures_mints._controls._clique import mints_clique
#
from verses._essence import build_essence, retrieve_essence
#
#
import somatic
from ventures.clique import ventures_clique
#
#
import click
import rich
#
#\

def clique ():
	build_essence ()

	'''
		This configures the verses module.
	'''
	#verses.start ()

	@click.group ()
	def group ():
		pass
	
	@group.command ("school")
	def controls ():
		import pathlib
		from os.path import dirname, join, normpath
		this_directory = pathlib.Path (__file__).parent.resolve ()
		this_module = str (normpath (join (this_directory, "../..")))

		
		somatic.start ({
			"directory": this_module,
			"extension": ".s.HTML",
			"relative path": this_module
		})
		
		import time
		while True:
			time.sleep (1)

	@group.command ("show-essence")
	def controls ():
		essence = retrieve_essence ()
		
		rich.print_json (data = essence)



	group.add_command (ventures_clique ({
		"ventures": retrieve_ventures ()
	}))

	group.add_command (treasures_clique ())
	group.add_command (mints_clique ())

	#group.add_command (clique_treasures ())
	group.add_command (trends_clique ())
	
	#group.add_command (trends_group.add ())
	
	group ()




#
