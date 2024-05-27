




'''
	from verses.frontiers.ventures import retrieve_ventures
	ventures = retrieve_ventures ()
'''

#/
#
from .monetary.venture import monetary_venture
from .sanique.venture import sanique_venture
from .vv_turbo.venture_build import bun_venture_build	
from .vv_turbo.venture_dev import bun_venture_dev	
from .demux_hap.venture import demux_hap_venture
#
#
from theme_park._essence import retrieve_essence
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
			monetary_venture (),
			sanique_venture (),
			bun_venture_build (),
			demux_hap_venture ()
		]
	})