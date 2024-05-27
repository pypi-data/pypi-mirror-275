


#----
#
#
from verses.adventures.monetary.quests.enumerate_passes import enumerate_passes
#
from verses.adventures.monetary.DB.safety.passes.document.insert import insert_pass
#
#
import click
#
#----

def clique_trends ():
	@click.group ("trends")
	def group ():
		pass


	@group.command ("insert-bracket")
	def on ():
		insert_pass ({
			"document": {
				"name": "pass 1"
			}
		})


	@group.command ("enumerate-passes")
	#@click.option ('--example-option', required = True)
	def on ():
		print ("on")
		
		enumerate_passes ()

	return group




#



