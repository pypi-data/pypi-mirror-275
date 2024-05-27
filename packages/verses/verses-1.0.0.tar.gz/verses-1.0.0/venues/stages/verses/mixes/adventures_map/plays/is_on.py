

'''
	# Replace 'your_pid_here' with the actual PID you want to check
	pid_to_check = your_pid_here
	status = check_process_status (pid_to_check)
	print ("Process status:", status)
'''
import psutil
def is_process_on (pid):
	try:
		exists = psutil.pid_exists (pid)
		if (exists == True):
			return "on"
		
		return "off"

	except Exception as E:
		print ("process status exception:", E)
		
	return "unknown";


import time
def check_is_on (packet):
	name = packet ["name"]

	is_on_check = packet ["is_on"]
	wait_for = packet ["wait_for"]

	loop = 0
	while True:
		the_status = is_on_check ()
		if (the_status == wait_for):
			break;
		
		time.sleep (1)

		loop += 1
		if (loop == 10):
			raise Exception (
				f"An anomaly occurred: { name } is { the_status } instead of { wait_for }"
			)

	



	
def is_on (packet):
	the_map = packet ["the_map"]
	
	with open (the_map, 'r') as FP:
		bracket = json.load (FP)
	
	#print ("bracket:", bracket)
	
	print ()
	print ("status:")
	
	for adventure in bracket:
		adventure_details = bracket [ adventure ]
		
		process_identity = adventure_details ["process_identity"]
		status = is_process_on (process_identity)
		print (f'    [{ status }] :: "{ adventure }" { process_identity }"')
		
	print ()

	return;	

