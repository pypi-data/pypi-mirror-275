

'''
	from goodest.adventures.sanique._ops.on as turn_on_sanique
	turn_on_sanique ()
'''


'''
	sanic /goodest/venues/stages/goodest/adventures/sanique/harbor/on.proc.py
'''

#----
#
#
from ..utilities.has_sanic_check import has_sanic_check
from .status import check_sanique_status
#
from goodest._essence import retrieve_essence
#
#
from biotech.topics.show.variable import show_variable
#
#
import atexit
import json
import multiprocessing
import subprocess
import time
import os
import shutil
import sys
import time
#
#----


	

def floating_process (procedure, CWD, env):
	show_variable ("procedure:", procedure)
	process = subprocess.Popen (
		procedure, 
		cwd = CWD,
		env = env
	)
	
	pid = process.pid
	
	show_variable ("sanic pid:", pid)

def turn_on_sanique (packet = {}):
	essence = retrieve_essence ()

	has_sanic_check ()

	the_status = check_sanique_status ()
	if (the_status == "on"):
		show_variable ("sanic is already on")		
		return;

	harbor_port = essence ["sanique"] ["port"]
	harbor_path = essence ["sanique"] ["directory"]

	env_vars = os.environ.copy ()
	env_vars ["USDA_food"] = essence ["USDA"] ["food"]
	env_vars ["NIH_supp"] = essence ["NIH"] ["supp"]
	env_vars ['inspector_port'] = essence ["sanique"] ["inspector"] ["port"]
	env_vars ['PYTHONPATH'] = ":".join (sys.path)
	env_vars ['essence'] = json.dumps (retrieve_essence ())


	'''
		cd /habitat_physical/.venv/lib/python3.12/site-packages/goodest/adventures/sanique
inspector_port=7457 /habitat_physical/.venv/bin/python /habitat_physical/.venv/bin/sanic harbor:create --port=8000 --host=0.0.0.0 --factory --fast --no-access-logs > /dev/null &
	'''
	the_procedure =  [
		"sanic",
		f'harbor:create',
		f'--port={ harbor_port }',
		f'--host=0.0.0.0',
		'--factory',
		
		#'--dev'
	]

	if (essence ["mode"] == "nurture"):
		the_procedure.append ("--workers=2")
	else:
		the_procedure.append ("--fast")
		

	process = floating_process (
		procedure = the_procedure,
		CWD = harbor_path,
		env = env_vars
	)
	
	
	loop = 0
	while True:
		show_variable ("checking sanique status")
	
		the_status = check_sanique_status ()
		if (the_status == "on"):
			break;
		
		time.sleep (1)

		loop += 1
		if (loop == 20):
			raise Exception ("Sanique doesn't seem to be turning on.")

	return;