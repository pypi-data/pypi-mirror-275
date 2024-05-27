




def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_folder = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

add_paths_to_system ([
	'../../../stages',
	'../../../stages_pip'
])


import json
import pathlib
from os.path import dirname, join, normpath


this_module_name = ""

this_folder = pathlib.Path (__file__).parent.resolve ()
structures = str (normpath (join (this_folder, "../../../../venues")))

this_module = str (normpath (join (structures, "stages", this_module_name)))

#status_assurances_path = str (normpath (join (this_folder, "insurance")))
status_assurances_path = str (normpath (join (this_folder, "..")))

import sys
if (len (sys.argv) >= 2):
	glob_string = status_assurances_path + '/' + sys.argv [1]
	db_directory = False
else:
	glob_string = status_assurances_path + '/**/API_status_*.py'
	db_directory = normpath (join (this_folder, "DB"))

print ("glob string:", glob_string)

import biotech
scan = biotech.start (
	glob_string = glob_string,
	simultaneous = True,
	module_paths = [
		normpath (join (structures, "stages")),
		normpath (join (structures, "stages_pip"))
	],
	relative_path = status_assurances_path,
	
	db_directory = db_directory
)
