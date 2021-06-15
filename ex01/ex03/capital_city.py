#! /usr/bin/env python3

import sys

def		capital_city():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
		}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
		}
	
	if len(sys.argv) == 2:
		if sys.argv[1] in states:
			city_code = states[sys.argv[1]]
			print(capital_cities[city_code])
		else:
			print("Unknown state")

if __name__=='__main__':
	capital_city()