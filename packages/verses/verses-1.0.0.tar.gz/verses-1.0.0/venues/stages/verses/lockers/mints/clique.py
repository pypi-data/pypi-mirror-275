



import verses.mints.names as mints_names
#import verses.modules.moves.save as save

def clique ():
	import click
	@click.group ("mints")
	def group ():
		pass


	'''
		verses mints names
	'''
	import click
	@group.command ("enumerate")
	def names ():
		the_names = mints_names.start ()
		sorted_mints_names = sorted (the_names)
	
		for name in sorted_mints_names:
			print (name)
	
		return;

	'''
		verses mints send-to-trends --name "mint-1"
	'''
	import click
	@group.command ("send-to-trends")
	@click.option ('--name', required = True)
	def search (name):
		#print ("name:", name)
		#print ('not yet implemented')
		
		#save.save (
		#	name = name
		#)
	
		return;

	return group




#



