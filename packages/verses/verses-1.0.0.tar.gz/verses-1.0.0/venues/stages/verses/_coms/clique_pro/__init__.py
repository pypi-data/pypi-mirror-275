




#from .group import clique as clique_group







#----
#
import verses
import verses._coms.clique_pro.group.trends as trends_group
import verses.modules.moves.save as save
from verses.adventures._controls.on import turn_on
from verses.adventures._controls.off import turn_off	
#
from verses.adventures._controls._clique import adventures_clique
from verses.lockers.treasures.clique import clique_treasures
from verses.lockers.trends.clique import clique_trends
#
from verses.mints import clique as mints_group
from verses.treasuries import clique as treasuries_group
#
from verses._essence import build_essence, retrieve_essence
#
#
import click
import rich
#
#----

def clique ():
	build_essence ()

	'''
		This configures the verses module.
	'''
	#verses.start ()

	@click.group ()
	def group ():
		pass
	
	@group.command ("controls")
	def controls ():
		import pathlib
		from os.path import dirname, join, normpath
		this_directory = pathlib.Path (__file__).parent.resolve ()
		this_module = str (normpath (join (this_directory, "../..")))

		import somatic
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

	@group.command ("on")
	def controls ():
		turn_on ()

	@group.command ("off")
	def controls ():
		turn_off ()

	group.add_command (adventures_clique ())
	group.add_command (clique_treasures ())
	group.add_command (clique_trends ())
	
	group.add_command (mints_group.clique ())
	#group.add_command (trends_group.add ())
	
	group ()




#
