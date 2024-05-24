

#----
#
from .build import build_squishy
#
#	
import click
import time
#
#----

def squishy_clique ():

	@click.group ("squishy")
	def group ():
		pass

	@group.command ("build")
	def on ():
		build_squishy ()
		return;
		
	@group.command ("rules")
	def on ():
		return;


	return group




#



