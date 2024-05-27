

#----
#
from verses.adventures._controls.on import turn_on
from verses.adventures._controls.off import turn_off
from verses.adventures._controls.refresh import refresh
from verses.adventures._controls.status import check_status
#
#
from ..monetary._controls._clique import monetary_clique
from ..squishy._controls._clique import squishy_clique
#
#
import click
#
#----

def adventures_clique ():
	@click.group ("adventures")
	def group ():
		pass


	
	
	#
	#	verses on
	#
	@group.command ("on")
	def on ():		
		turn_on ()

	
	@group.command ("off")
	def off ():
		turn_off ()

	@group.command ("refresh")
	def refresh_op ():
		refresh ()

	@group.command ("status")
	def status ():
		check_status ()

	group.add_command (monetary_clique ())
	group.add_command (squishy_clique ())


	return group




#



