

'''
	itinerary:
		[ ] pass the current python path to this procedure
'''


'''
	https://sanic.dev/en/guide/running/manager.html#dynamic-applications
'''

'''
	worker manager:
		https://sanic.dev/en/guide/running/manager.html
'''

'''
	Asynchronous Server Gateway Interface, ASGI:
		https://sanic.dev/en/guide/running/running.html#asgi
		
		uvicorn harbor:create
'''

'''
	Robyn, rust
		https://robyn.tech/
'''

'''
	--factory
'''

#----
#
''''
	addresses
"'''
#
from .sockets_guest import sockets_guest
#
from verses.adventures.sanique.utilities.generate_inventory_paths import generate_inventory_paths
#
from verses._essence import retrieve_essence, build_essence
from verses.adventures.alerting import activate_alert
from verses.adventures.alerting.parse_exception import parse_exception
#
#
from biotech.topics.show.variable import show_variable
#
#
import sanic
from sanic import Sanic
from sanic_ext import openapi
#from sanic_openapi import swagger_blueprint, openapi_metadata
#from sanic_openapi import swagger_blueprint, doc
import sanic.response as sanic_response
#
#
import json
import os
import traceback
#
#----

'''
	https://sanic.dev/en/guide/running/running.html#using-a-factory
'''
def create ():
	env_vars = os.environ.copy ()
	essence_path = env_vars ['essence_path']
	
	build_essence ({
		"essence_path": essence_path
	})
	
	essence = retrieve_essence ()
	inspector_port = essence ["sanique"] ["inspector"] ["port"]
	

	app = Sanic (__name__)
	
	app.extend (config = {
		"oas_url_prefix": "/docs",
		"swagger_ui_configuration": {
			"docExpansion": "list" # "none"
		}
	})
	
	#app.blueprint(swagger_blueprint)
	
	#
	#
	#	https://sanic.dev/en/guide/running/configuration.html#inspector
	#
	app.config.INSPECTOR = True
	app.config.INSPECTOR_HOST = "0.0.0.0"
	app.config.INSPECTOR_PORT = int (inspector_port)
	
	#
	#	opener
	#
	#
	#app.ext.openapi.add_security_scheme ("api_key", "apiKey")
	app.ext.openapi.add_security_scheme ("api_key", "http")
	
	async def websocket_handler(request, ws):
		while True:
			data = await ws.recv()
			await ws.send ("You sent: " + data)

	@app.websocket("/websocket_route")
	async def websocket_route(request, ws):
		await websocket_handler(request, ws)

	@app.patch ("/patch_route")
	async def patch_handler(request):
		data = request.json

		return json ({
			"message": "Received PATCH request", 
			"data": data
		})

		
	return app

