




'''
	from verses.frontiers.ventures import retrieve_ventures
	ventures = retrieve_ventures ()
'''

#/
#
from .adventures_trends.monetary.venture import trends_monetary_venture
#
#
from verses._essence import retrieve_essence
#
#
from ventures import ventures_map
#
#\

def retrieve_ventures ():
	essence = retrieve_essence ()

	return ventures_map ({
		"map": essence ["ventures"] ["path"],
		"ventures": [
			trends_monetary_venture ()
		]
	})