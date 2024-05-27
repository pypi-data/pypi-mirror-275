
'''
	python3 insurance.proc.py rides.season_1/TR/_status/status_2.py
'''

import theme_park.rides.season_1.TR as TR_indicator

from rich import print_json

def check_1 ():	
	places = [{
		"high": 38404.3875,
		"low": 36901.035,
		"close": 38056.5515
	},
	{
		"high": 38423.07,
		"low": 37602.688,
		"close": 37895.439
	},
	{
		"high": 38251.5645,
		"low": 37514.59,
		"close": 38153.885
	},
	{
		"high": 39002.916,
		"low": 38082.745,
		"close": 38768.4165
	}]
	
	TR_indicator.calc (
		#
		#	data 
		#
		places = places
	)
	
	print_json (data = places)
	
	
	assert (places [1] ["true range"] == 820.3819999999978)
	assert (places [2] ["true range"] == 736.9745000000039), places [2]
	assert (places [3] ["true range"] == 920.1709999999948), places [3]
	
	
checks = {
	'check 1': check_1
}