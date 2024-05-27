
'''
	from verses.adventures.sanique.adventure import sanique_adventure
	sanique_adventure ()
'''

from verses.adventures.sanique._controls.on as turn_on_sanique
from verses.adventures.sanique._controls.off as turn_off_sanique

def sanique_adventure ():
	return {
		"turn on": turn_on_sanique,
		"turn off": turn_off_sanique,
		"is on": lambda s : s	
	}